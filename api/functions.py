import os, glob
import subprocess
import logging
import datetime
# from api.createskiplist import skip

logging.basicConfig(filename='all_rendered_shots.txt', level=logging.DEBUG, filemode='a', format='%(message)s %(asctime)s')

# get the current date and time'
def shot_name2num(filename):
    filename = os.path.basename(filename) 
    raw_ver_num = filename.split('_')[0]
    aidx = (ord('a') - ord(raw_ver_num[0].lower())) * 100
    true_ver_num = aidx + int(raw_ver_num[1:])
    return true_ver_num

now = datetime.datetime.now()
def render_latests(cfg, skipfile = 'skiplist.txt'):
    test_shots = search_for_shots(cfg.SEARCH_DIR)
    
    # open the text file in read mode
    with open(skipfile, 'r') as file:
        # read the contents of the file
        skiplist = []
        for line in file.readlines():
            skiplist.append(line.strip()) # Remove newline characters

    for shot in sorted(test_shots, key=shot_name2num):
        if shot in skiplist:
            continue

        latest_version = min(test_shots[shot], key=lambda ext: cfg.RENDER_ORDER.get(ext.upper(), 1000))
        print(f"Rendering {test_shots[shot][latest_version]}")
        # completed = subprocess.run([cfg.HARMONY_EXE,"-batch",fname], shell=True, capture_output=True)
        # logging.debug(f'{typ}, {jname}')
        # print(completed)

def search_for_shots(dir):
    #A01_CMP_JDoe {idx}{typ}{shot_name}.xstage
    shots = dict()
    for fname in glob.glob(os.path.join(dir,"*.xstage"), recursive=True):
        data = os.path.basename(fname).split("_")
        snum = data[0]
        typ = data[1]
        if snum not in shots:
            shots[snum] = dict()
        if typ not in shots[snum]:
            shots[snum][typ] = fname
    return shots

if __name__ == "__main__":
    # Example usage
    class Config:
        SEARCH_DIR = "C:/path/to/search/dir"
        HARMONY_EXE = "C:/path/to/harmony.exe"
        RENDER_ORDER = {"CMP": 0, "PNT": 1, "CLN": 2, "RUF": 3, "POS": 4}
        
    cfg = Config()
    cfg.SEARCH_DIR = "/Users/willwalker/Harmony_Batch_Renderer/test_shots/"

    render_latests(cfg)
