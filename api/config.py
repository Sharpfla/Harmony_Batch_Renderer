import os
class config:
    SEARCH_DIR=r"R:\APS\APSFleischer\SCREAM WRITERS EDIT\Batch\Harmony_Batch_Renderer\test_shots"

    # You can update these paths to include support for new versions
    VERBOSE = False
    INSTALL_DIR = r"R:\APS\APSFleischer\SCREAM WRITERS EDIT\Batch\Harmony_Batch_Renderer"

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
