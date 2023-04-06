import os
class Config:
    SEARCH_DIR=r"F:\root\2022.anim.proj.APSscreamwriters\shots\CMP\C_SEQ"

    # You can update these paths to include support for new versions
    VERBOSE = False
    INSTALL_DIR = r"C:\Users\Sharp\Harmony_Batch_Renderer"
    RENDER_ORDER = {"CMP": 0, "PNT": 1, "CLN": 2, "RUF": 3, "POS": 4}
        
    supported_harmony_exes = {
        "V20": r"C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 20 Premium",
        "V21": r"C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 21 Premium",
        "V21.1": r"C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 21.1 Premium",
        "V22": r"C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 22 Premium"
    }
    SELECTED_HARMONY_VERSION = "V22"
    HARMONY_EXE = os.path.join(supported_harmony_exes[SELECTED_HARMONY_VERSION], \
        r"win64\bin\HarmonyPremium.exe")

    version_found = os.path.isfile(HARMONY_EXE)

    if not version_found:
        raise(RuntimeError(f"The selected version: {HARMONY_EXE} \nCould not be Found \n Exiting....."))
