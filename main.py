import os
import time
import cson

def parse_file(filename, root_note_path):
    # Parse the .cson, returning a dictionary that can be accessed more easily.
    # root_note_path and filename must be joined into a single path to allow for files to be accessed even when main.py is not running from the same directory.
    with open(os.path.join(root_note_path,filename), "r", errors="ignore") as f:
        parsed_cson = cson.load(f)

    # The note title gets used as the filename, so sanitise it to remove any problem characters (e.g. \).
    def sanitise_title(title):
        forbidden_chars = ["/", "\\", "<", ">", ":", "\"", "|", "?", "*"]    
        title = "".join([x if x not in forbidden_chars else "_" for x in title])
        return title

    title = sanitise_title(parsed_cson["title"])

    # Empty notes return a KeyError, since there is no content. Set content to empty string in this case, so they can still be exported correctly.
    try:
        content = parsed_cson["content"]
    except KeyError:
        content = ""

    createdAt = parsed_cson["createdAt"]
    modifiedAt = parsed_cson["updatedAt"]
    folder = parsed_cson["folder"]

    # Create the respective folder for the note to be placed in.
    output_dir = os.path.join(root_note_path,"Output",folder)
    try:
        # os.makedirs will (try to) create the entire folder structure from left to right, not just the rightmost file.
        os.makedirs(output_dir)
    except FileExistsError:
        # Directory already made, so continue.
        pass

    # Open a new Markdown file in its respective folder, and write the contents of the .cson file to it.
    with open(output_dir+"\\"+title+".md", "w") as output:
        output.write(content)

root_note_path = str(input("Enter the filepath to your Boostnote files:\n"))
file_list = os.listdir(root_note_path)
print(file_list)

for filename in file_list:
    parse_file(filename, root_note_path)