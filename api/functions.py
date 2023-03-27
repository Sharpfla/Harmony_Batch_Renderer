import os, glob
import subprocess

def find_xstage_files(dir, sort = False):
    names = glob.glob(os.path.join(dir,"**\\*.xstage"), recursive=True)
    return names

def group_xstage_files(dir):
    #A01_CMP_JDoe  {idx}{typ}{shot_name}.xstage
    shots = dict()
    for fname in find_xstage_files(dir):
        data = os.path.basename(fname).split("_")
        snum = data[0]
        typ = data[1]
        name = "_".join(data[2:]).strip()

        if name not in shots:
            shots[name] = dict()
        if snum not in shots[name]:
            shots[name][snum] = dict()
        shots[name][snum][typ.upper()] = fname
    return shots

def render_latests(cfg):
    jobs = group_xstage_files(cfg.SEARCH_DIR)
    for jname, jdata in jobs.items():
        for snum, version_data in jdata.items():
            typ = None
            # Search for .xstage files containing "CMP" in the filename and write their paths to the output file
            if "CMP" in version_data:
                typ = "CMP"
                fname = os.path.abspath(version_data['CMP'])
            elif "PNT" in version_data:
                typ = "PNT"
                fname = os.path.abspath(version_data['PNT'])
            elif "CLN" in version_data:
                typ = "CLN"
                fname = os.path.abspath(version_data['CLN'])
            if typ != None:
                print(snum, typ, jname)
                completed = subprocess.run([cfg.HARMONY_EXE,"-batch",fname], shell=True, capture_output=True)
                print(completed)


if __name__ == "__main__":
    render_latests()
