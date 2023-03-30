This tool renders multiple harmony file by searching a directory for xstage files following its naming convention
the newest version of a shot is determined by this naming convention

SETUP

1. The file naming convention is A1_POS_JDoe.
- The shot numbers are listed A01-Z99.
- Rendering for newest file order is CMP > PNT > CLN > RUF > POS.

2. Enter api\config.py and adjust the settings.
    - Set the SEARCH_DIR to the location of your harmony files.
    - Change INSTALL_DIR to the location of batch renderer's repository.
    - Change SELECTED_HARMONY_VERSION to the version installed on you machine.

4. Edit skiplist.txt
    - the skip list will skip shot numbers you don't want to render.
    - "A01" and "A1" are NOT the same shot to the skiplist. If you're not sure which to use list both.
    - Add a comma after each entry EXCEPT the last entry.

3. Run main.py
    - Say no to changing search directory (will be better implemented in later versions).
    - Enter the same harmony version as you entered in config.py.
    - every rendered shot is logged in all_rendered_shots.txt.

Future goals:
    I'd like to add use of harmony's javascript library to allow specifying resolution, output type, and output location.