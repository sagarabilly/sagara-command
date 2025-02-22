"""
------Simple Rename------
------PYTHON 3.11.5------
----------UTF-08---------

SAGARA - 241014
"""

import os
import argparse
import pandas as pd


def rename_files_mimic(folder_a, folder_b):
    files_a = sorted(os.listdir(folder_a))
    files_b = sorted(os.listdir(folder_b))

    for i in range(min(len(files_a), len(files_b))):
        old_file_path = os.path.join(folder_b, files_b[i])
        new_file_name = files_a[i]
        new_file_path = os.path.join(folder_b, new_file_name)
        os.rename(old_file_path, new_file_path)

    print(f"Files in {folder_b} renamed successfully to match {folder_a}.")


def rename_files_from_csv(folder_b, csv_path, column_name):
    df = pd.read_csv(csv_path)
    if column_name not in df.columns:
        print(f"Column '{column_name}' does not exist in the CSV file.")
        return

    new_names = df[column_name].dropna().tolist()
    files_b = sorted(os.listdir(folder_b))

    for i in range(min(len(new_names), len(files_b))):
        old_file_path = os.path.join(folder_b, files_b[i])
        new_file_name = new_names[i]
        new_file_path = os.path.join(folder_b, new_file_name)
        os.rename(old_file_path, new_file_path)

    print(
        f"Files in {folder_b} renamed successfully based on the CSV list from {csv_path}."
    )


def rename_files_from_txt(folder_b, txt_path):
    with open(txt_path, "r") as file:
        new_names = [line.strip() for line in file.readlines()]

    files_b = sorted(os.listdir(folder_b))

    for i in range(min(len(new_names), len(files_b))):
        old_file_path = os.path.join(folder_b, files_b[i])
        new_file_name = new_names[i]
        new_file_path = os.path.join(folder_b, new_file_name)
        os.rename(old_file_path, new_file_path)

    print(
        f"Files in {folder_b} renamed successfully based on the text file list from {txt_path}."
    )


def rename_files_to_numbers(folder_b):
    files_b = sorted(os.listdir(folder_b))

    for i, file_name in enumerate(files_b, start=1):
        old_file_path = os.path.join(folder_b, file_name)
        ext = os.path.splitext(file_name)[1]  # Keep the original extension
        new_file_name = f"{i}{ext}"
        new_file_path = os.path.join(folder_b, new_file_name)
        os.rename(old_file_path, new_file_path)

    print(f"Files in {folder_b} renamed to sequential numbers successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This command will help you rename files automatically with ease."
    )
    parser.add_argument(
        "--mimic",
        action="store_true",
        help="Rename files in Target Folder (Folder B) to match names in Folder A.",
    )
    parser.add_argument(
        "--csv",
        nargs=2,
        help="Rename files in Target Folder (Folder B) based on a CSV file. Provide CSV file path and column name.",
    )
    parser.add_argument(
        "--txt",
        nargs=1,
        help="Rename files in Target Folder (Folder B) based on a text file. Provide text file path.",
    )
    parser.add_argument(
        "--number",
        "-n",
        action="store_true",
        help="Rename files in Target Folder (Folder B) to a number sequence with original extensions.",
    )
    parser.add_argument("folder_b", type=str, help="Path to Folder B")
    parser.add_argument(
        "folder_a", type=str, nargs="?", help="Path to Folder A (required for --mimic)"
    )

    args = parser.parse_args()

    if args.mimic:
        if not args.folder_a:
            print("Both Folder A and Folder B are required for the --mimic option.")
        else:
            rename_files_mimic(args.folder_a, args.folder_b)
    elif args.csv:
        csv_path, column_name = args.csv
        rename_files_from_csv(args.folder_b, csv_path, column_name)
    elif args.txt:
        txt_path = args.txt[0]
        rename_files_from_txt(args.folder_b, txt_path)
    elif args.number:
        rename_files_to_numbers(args.folder_b)
    else:
        print("Please use either --mimic, --csv, --txt, or --number option.")
