@echo off
setlocal enabledelayedexpansion

set "search_dir=D:\root\2022.anim.proj.APSscreamwriters\shots\CMP\C SEQ"
set "output_file=D:\root\2022.anim.proj.APSscreamwriters\shots\CMP\output.txt"

rem Search for .xstage files containing "CMP" in the filename and write their paths to the output file
(for /r "%search_dir%" %%a in (*.xstage) do (
    set "filename=%%~na"
    set "extension=%%~xa"
    if /i "!filename:CMP=!" neq "!filename!" (
        echo %%a
    )
)) > "%output_file%"

rem Loop through the output file and run the command for each file path
for /f "delims=" %%a in (%output_file%) do (
  echo Running command for file: "%%a"
  "C:\Program Files (x86)\Toon Boom Animation\Toon Boom Harmony 21 Premium\win64\bin\HarmonyPremium.exe" -batch "%%a"
)

rem Delete the output file
del "%output_file%"
