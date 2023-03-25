@echo off
call:%~1
goto exit

setlocal enabledelayedexpansion

duplicate_ver_check:
  @REM set "dir_path="
  @REM set "output_file="
  
  set dir_path = %1
  set output_file = %2
  if "%1"=="" set dir_path="E:\root\2022.anim.proj.APSscreamwriters\shots\CMP\C SEQ"
  if "%2"=="" set output_file="E:\root\2022.anim.proj.APSscreamwriters\tech dev\outputlist.txt"

  echo Searching for .xstage files in %dir_path% ...
  for /L %%i in (1,1,99) do (
    for %%j in (A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z) do (
      set "prefix=%%j%%i"
      set "count=0"
    echo %%j%%i
      for /r "%dir_path%" %%k in ("!prefix!*xstage") do (
        set /a count+=1
        if !count! == 1 (
          set "prev_file=%%k"
        ) else (
          set "curr_file=%%k"
          for %%l in ("!prev_file!") do set "prev_name=%%~nl"
          for %%l in ("!curr_file!") do set "curr_name=%%~nl"
          set "prev_prefix=!prev_name:~0,3!"
          set "curr_prefix=!curr_name:~0,3!"
          if !prev_prefix! == !curr_prefix! (
            echo WARNING: Files with the same prefix found:
            echo !prev_file!
            echo !curr_file!
            echo.
          )
          set "prev_file=!curr_file!"
        )
        echo Found file: %%k
        set "filename=%%~nk"
        if "!filename!"=="*CMP*" (
          echo %%k >> "%output_file%"
        )
      )
    )
  )
  echo Done! Output saved to "%output_file%"
  Pause
