
@echo off
REM =====================================================
REM Batch Script to Check Installed Programs and Versions
REM =====================================================

REM Enable delayed variable expansion for dynamic variable handling
setlocal enabledelayedexpansion

REM Initialize counters and variables
set /a total=0
set /a success=0
set "missing_list="

REM =====================================================
REM Define the list of programs and their version commands
REM =====================================================
REM Format:
REM   ProgramName "Version Command"
REM Example: Python "python --version"

rem You can add or remove programs below as needed
set "programs[1]=Python|python --version"
set "programs[2]=Pip|pip --version"
set "programs[3]=MYSQL|mysql --version"
set "programs[4]=NPM|npm --version"
set "programs[5]=Node.js|node --version"
set "programs[6]=Dotnet|dotnet --version"
set "programs[7]=Git|git --version"
set "programs[8]=NeoVim|nvim --version"
set "programs[9]=Anaconda|conda --version"
set "programs[10]=GoLang|go version"
set "programs[11]=Rustc|rustc --version"
set "programs[12]=Cargo|cargo --version"
set "programs[13]=Gnu C Compiler|gcc --version"
set "programs[14]=Pandoc| pandoc --version"
set "programs[15]=Scoop| scoop --version"

REM Total number of programs to check
set /a total=15

echo =====================================================
echo       Checking Installed Programs and Versions
echo =====================================================
echo              PROGRAM REQUIREMENT CHECKER
echo                    - sagara_billy -
echo.

REM Iterate through each program and check its installation
for /L %%i in (1,1,%total%) do (
    REM Extract program name and version command
    for /F "tokens=1,2 delims=|" %%a in ("!programs[%%i]!") do (
        set "progName=%%a"
        set "versionCmd=%%b"
    )

    echo Checking !progName!...

    REM Attempt to execute the version command
    REM Redirect output to nul to suppress it
    cmd /c "!versionCmd!" >nul 2>&1

    REM Check the outcome of the version command
    if !errorlevel! == 0 (
        echo   !progName! is installed.
        set /a success+=1
    ) else (
        echo   !progName! is NOT installed.
        echo please check the environment variables
        set "missing_list=!missing_list! !progName!"
    )
    echo.
)

REM =====================================================
REM Display Summary of Results
REM =====================================================
echo =====================================================
if %success% EQU %total% (
    echo %success%/%total% All programs successfully installed.
) else (
    echo %success%/%total% programs successfully installed.
    echo Missing Programs:%missing_list%
)
echo =====================================================

REM End of script
endlocal
pause

