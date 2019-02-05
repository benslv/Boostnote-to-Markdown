import time

def parse_time(time_str):
    i_date = time_str[:10]
    i_time = time_str[11:23]

    i_date = list(map(int, i_date.split("-")))
    i_time = list(map(float, i_time.split(":")))

    # time.mktime used to convert human-readable time to epoch time that can be used to update file's utime.
    t = (i_date[0], i_date[1], i_date[2], int(i_time[0]), int(i_time[1]), int(round(i_time[2],0)), 0, 0, -1)
    output_time = time.mktime(t)

    return(output_time)