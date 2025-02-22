
# Simple Rename (`srename.py`)

`Simple Rename` is a Python script that automates file renaming in different ways. It supports renaming files to match another folder, using a CSV or TXT file, or renaming files sequentially with numbers. This tool simplifies batch renaming tasks efficiently.

## Features
- **Mimic Mode**: Renames files in a target folder (`Folder B`) to match the names in a source folder (`Folder A`).
- **CSV-Based Renaming**: Renames files in a target folder based on names from a specified column in a CSV file.
- **TXT-Based Renaming**: Renames files in a target folder based on a list of names from a TXT file.
- **Number Sequence Renaming**: Renames files in a target folder to a numerical sequence while preserving their extensions.

## Installation  
### Requirements  
- Python 3.11.5 or later  
- You need to install pandas for this:  
```sh
pip install pandas
```

### Running the Script  
Ensure the script is executable and placed in a directory available in your system's `PATH` (See the main README.md).  
If using Windows, you can create a batch file (`srename.bat`) for easy execution.  

## Usage  
Run the script using the following commands:  

### 1. Mimic Mode  
Renames files in `Folder B` to match `Folder A`.
```sh
srename --mimic /path/to/folder_b /path/to/folder_a
```

### 2. Rename Using CSV File
Renames files in `Folder B` based on a CSV file.
```sh
srename --csv /path/to/folder_b /path/to/file.csv column_name
```
- `file.csv`: The CSV file containing the new names.
- `column_name`: The column in the CSV that contains new file names.

### 3. Rename Using TXT File
Renames files in `Folder B` based on a text file.
```sh
srename --txt /path/to/folder_b /path/to/file.txt
```
- Each line in the text file should contain one new filename.

### 4. Rename to Number Sequence
Renames all files in `Folder B` sequentially as `1.ext`, `2.ext`, etc.
```sh
srename --number /path/to/folder_b
```

## Notes
- The script processes files in lexicographic order.
- Ensure that the number of new names matches or exceeds the number of files in `Folder B` to prevent errors.

## Contributions
Please feel free to modify and any contributions are appreciated

