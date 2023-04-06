# A script that searches for all the xstage files in search_dir
# stores each new stage in an object containing snum, typ, and file location
# parses the snum as an int
# searches for each shot by typ priority
# renders each shot

import sys
import os

# class shot_data:
#     snum = None
#     typ = None
#     def __init__(self, snum, typ, ext) -> None:
#         shot_data.snum = snum
#         shot_data.typ = typ
#         shot_data.ext = ext


# search function can use lens to split path into in data (snum, typ, and ext).
# it stores the data in an array for the snum.
#first it checks the position in the array. It updates the array info(typ and ext)
# the new info is greater priority (POS > RUF > CLN > PNT > CMP).
        
def find_xstage_file(dir, snum, render_num, shot_list):
    for root, dir, files in os.walk(dir):
        for file in files:
            if file.startswith(snum) and file.endswith('.xstage'):
                filename_without_extension = os.path.splitext(file)[0]
                curr_shot_data = filename_without_extension.split('_')
                curr_shot_data.append(os.path.join(root, file))
        if curr_shot_data[1] > shot_list[render_num]:
            return curr_shot_data  # Return the list of file parts
        else: return shot_list[render_num]
    return None


def shot_search(self, dir):
        # array 0 is offset
        shot_list = []
        render_num = 0
        seq_list = [ '0', 'A', 'B','C' ,'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J' ,'K' ,'L','M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U' ,'V' ,'W' ,'X' ,'Y' ,'Z']
        while i in range(26):
            seq_num = seq_list[i]
            for x in range(100):
                snum = str(seq_num) + str(x)
                shot_list[render_num] = find_xstage_file(dir, snum)
        i = i + 1