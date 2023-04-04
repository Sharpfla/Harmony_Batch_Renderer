# A script that searches for all the xstage files in search_dir
# stores each new stage in an object containing snum, tyoe, and file location
# parses the snum as an int
# searches for each shot by tpye priority
# renders each shot

import sys

class Shot:
    def __init__(self, snum, typ) -> None:
        Shot.snum = snum
        Shot.type = typ

snum = 'A01'
typ = 'POS'

i = 0
d = {}
while i <= 99:
    d["shot{0}".format(i)] = Shot('A00', 'CMP')
    i = i + 1