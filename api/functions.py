import os, glob
import subprocess

#SEARCH_DIR="E:\root\2022.anim.proj.APSscreamwriters\shots\CMP\""
SEARCH_DIR="../test_shots"

def find_xstage_files(sort = False):
    names = glob.glob(os.path.join(SEARCH_DIR,"*.xstage"))
    return names

def group_xstage_files():
    #A01_CMP_JDoe  {idx}{typ}{shot_name}.xstage
    groups = dict()
    for fname in find_xstage_files():
        fname = os.path.basename(fname)
        data = fname.split("_")
        ver = data[0]
        typ = data[1]
        shot_name = "_".join(data[2:])

        if shot_name not in groups:
            groups[shot_name] = dict()

        if ver not in groups[shot_name]:
            groups[shot_name][ver] = dict()
            groups[shot_name][ver]["types"] = set()
        groups[shot_name][ver]["types"].add(typ.upper())


def render_latests():
    jobs = group_xstage_files()
    for jname, jdata in jobs.items():
        latest_version = sorted(jdata)[-1]

        # Search for .xstage files containing "CMP" in the filename and write their paths to the output file
        if "CMP" in latest_version["types"]:
            subprocess.call([f"'C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 21 Premium\win64\bin\HarmonyPremium.exe' -batch {fname}"])
        elif "PNT" in latest_version["types"]:
            subprocess.call([f"'C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 21 Premium\win64\bin\HarmonyPremium.exe' -batch {fname}"])
if __name__ == "__main__":
    render_latests()
    pass      
# # Searching for xstage files with CMP, PNT, or CLN in their filename in %search_dir% and its subfolders...

# if exist %output_file% del %output_file%

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
    
# )