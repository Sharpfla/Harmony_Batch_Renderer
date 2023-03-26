import os, glob
import subprocess

#SEARCH_DIR="E:\root\2022.anim.proj.APSscreamwriters\shots\CMP\""
SEARCH_DIR="E:\\root\\2022.anim.proj.APSscreamwriters\\shots\\CMP\\C_SEQ"
HARMONY_EXE = "C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 22 Premium\win64\bin\HarmonyPremium.exe"

def find_xstage_files(sort = False):
    names = glob.glob(os.path.join(SEARCH_DIR,"**\\*.xstage"), recursive=True)
    return names

def group_xstage_files():
    #A01_CMP_JDoe  {idx}{typ}{shot_name}.xstage
    shots = dict()
    for fname in find_xstage_files():
        data = os.path.basename(fname).split("_")
        snum = data[0]
        typ = data[1]
        name = "_".join(data[2:]).strip()
        # print(f"Name:{name}\nVer:{snum}\nTyp:{typ}\nPath:{fname}\n\n")

        if name not in shots:
            shots[name] = dict()
        if snum not in shots[name]:
            shots[name][snum] = dict()
        shots[name][snum][typ.upper()] = fname
    return shots

def render_latests():
    jobs = group_xstage_files()
    # print (*list(jobs.keys()), sep="\n")
    for jname, jdata in jobs.items():
        # latest_version_idx = sorted(jdata)[-1]
        for snum, version_data in jdata.items():
            # latest_version = jdata[latest_version_idx]

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
                # cmd = f"{HARMONY_EXE} -batch {fname}"
                completed = subprocess.run([HARMONY_EXE, '-batch', fname], shell=True, capture_output=True)
                print(completed)
                print(jname, snum, typ)
            # print(cmd)
    # print(jobs)
        
    
        # subprocess.call(cmd, shell=True)

        
if __name__ == "__main__":
    render_latests()

# for /d /r "%search_dir%" %%d in (*) do (
#     set cmp_file=
#     set pnt_file=
#     set cln_file=

#     for %%f in ("%%d\*.xstage") do (
#         set filename=%%~nf
#         set cmp=!filename:CMP=!
#         set pnt=!filename:PNT=!
#         set cln=!filename:CLN=!

#         if not "!cmp!"=="!filename!" (
#             set cmp_file=%%~ff
#         ) else if not "!pnt!"=="!filename!" (
#             set pnt_file=%%~ff
#         ) else if not "!cln!"=="!filename!" (
#             set cln_file=%%~ff
#         )
#  "C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 21 Premium\win64\bin\HarmonyPremium.exe" -batch "%%a"