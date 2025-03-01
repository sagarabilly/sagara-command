@echo off

echo Pandoc Markdown to HTML Conversion
if "%~1"=="" (
    echo Usage: webnote "path/to/input.md"
    exit /b 1
)

set "input_file=%~1"
set "output_file=%~dp0..\src\sagarawebnote\webnote.html"
REM set "css_file=%~dp0..\src\sagarawebnote\styles1.css"

pandoc "%input_file%" -o "%output_file%" --css="styles1.css" --standalone  

echo Conversion complete: "%output_file%"
echo Deploying Python http.server port 9995
python -m http.server 9995 --directory "%~dp0..\src\sagarawebnote"
