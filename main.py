import os
import time
import cson

def parse_file(filename, root_note_path):
    with open(os.path.join(root_note_path,filename), "r") as f:
        parsed_cson = cson.load(f)

    def sanitise_title(title):
        forbidden_chars = ["/", "\\", "<", ">", ":", "\"", "|", "?", "*"]    
        title = "".join([x if x not in forbidden_chars else "_" for x in title])
        return title

    title = sanitise_title(parsed_cson["title"])
    content = parsed_cson["content"]
    createdAt = parsed_cson["createdAt"]
    modifiedAt = parsed_cson["updatedAt"]
    folder = parsed_cson["folder"]

    output_dir = os.path.join("Output",folder)
    try:
        os.makedirs(output_dir)
    except FileExistsError:
        # Directory already made, so continue.
        pass

    with open(output_dir+"\\"+title+".md", "w") as output:
        output.write(content)

root_note_path = str(input("Enter the filepath to your Boostnote files:\n"))
file_list = os.listdir(root_note_path)
print(file_list)

for filename in file_list:
    parse_file(filename, root_note_path)