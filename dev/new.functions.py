# A script that searches for all the xstage files in search_dir
# stores each new stage in an object containing snum, tyoe, and file location
# parses the snum as an int
# searches for each shot by tpye priority
# renders each shot

import sys

class shot_data:
    snum = None
    typ = None
    def __init__(self, snum, typ, ext) -> None:
        shot_data.snum = snum
        shot_data.typ = typ
        shot_data.ext = ext
        

curr_shot_data = []
i = 1

# search function can use lens to split path into in data (snum, typ, and ext).
# it stores the data in an array for the snum.
#first it checks the position in the array. It updates the array info(typ and ext)
# the new info is greater priority (POS > RUF > CLN > PNT > CMP).

def search_n_update(self, snum, typ):
        search_n_update.snum = snum
        search_n_update.typ = typ
        if snum



# array 0 is offset
seq_list = [ '0', 'A', 'B','C' ,'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J' ,'K' ,'L','M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U' ,'V' ,'W' ,'X' ,'Y' ,'Z']

while i in range(26):
    seq_num = seq_list[i]
    for x in range(100):
        snum = [seq_num, x]
        # search function needs to go here
    i = i + 1


snum = 'A01'
typ = 'CMP'
ext = r"file\location"

curr_shot_data.append({'snum': snum, 'typ': typ, "ext": ext})
print(curr_shot_data)