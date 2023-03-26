@echo on
setlocal enabledelayedexpansion

set output_file=output.txt
set search_dir=E:\root\2022.anim.proj.APSscreamwriters\shots\CMP\

echo Searching for xstage files with CMP, PNT, or CLN in their filename in %search_dir% and its subfolders...

if exist %output_file% del %output_file%

for /d /r "%search_dir%" %%d in (*) do (
    set cmp_file=
    set pnt_file=
    set cln_file=

    for %%f in ("%%d\*.xstage") do (
        set filename=%%~nf
        set cmp=!filename:CMP=!
        set pnt=!filename:PNT=!
        set cln=!filename:CLN=!

        if not "!cmp!"=="!filename!" (
            set cmp_file=%%~ff
        ) else if not "!pnt!"=="!filename!" (
            set pnt_file=%%~ff
        ) else if not "!cln!"=="!filename!" (
            set cln_file=%%~ff
        )
    )

    if defined cmp_file (
        echo !cmp_file!>>%output_file%
    ) else if defined pnt_file (
        echo !pnt_file!>>%output_file%
    ) else if defined cln_file (
        echo !cln_file!>>%output_file%
    )
)

echo Done.
echo The following xstage files were found:
type %output_file%

pause>nul
