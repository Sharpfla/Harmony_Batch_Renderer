import os
class config:
    SEARCH_DIR=r"C:\Users\391524\Documents\test_shots\test_shots"
    # TOON_BOOM_PATH = r'C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 21 Premium\win64\bin'

    # You can update these paths to include support for new versions
    VERBOSE = False
    INSTALL_DIR = r"C:\Users\391524\Harmony_Batch_Renderer"
    # CONFIG_SCRIPT = os.path.join(INSTALL_DIR,"/api/scripts/renderconfig.js")

    supported_harmony_exes = {
        "V20": r"C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 20 Premium",
        "V21": r"C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 21 Premium",
        "V21.1": r"C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 21.1 Premium",
        "V22": r"C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 22 Premium"
    }
    SELECTED_HARMONY_VERSION = "V21"
    HARMONY_EXE = os.path.join(supported_harmony_exes[SELECTED_HARMONY_VERSION], \
        r"win64\bin\HarmonyPremium.exe")

    version_found = os.path.isfile(HARMONY_EXE)

    if not version_found:
        raise(RuntimeError(f"The selected version: {HARMONY_EXE} \nCould not be Found \n Exiting....."))

    # HARMONY_EXE += f" -config {CONFIG_SCRIPT} "