import os
import argparse
import random

def secure_delete_file(file_path, passes=3):
    try:
        length = os.path.getsize(file_path)
        with open(file_path, "ba+", buffering=0) as f:
            for _ in range(passes):
                f.seek(0)
                f.write(os.urandom(length))
                f.flush()
                os.fsync(f.fileno())
        # Truncate the file
        with open(file_path, "ba+", buffering=0) as f:
            f.truncate(0)
        os.remove(file_path)
        print(f"[+] Securely deleted: {file_path}")
    except Exception as e:
        print(f"[!] Error deleting {file_path}: {e}")

def secure_delete_folder(folder_path, recursive=False, passes=3):
    if recursive:
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                secure_delete_file(os.path.join(root, name), passes)
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except OSError:
                    pass
        try:
            os.rmdir(folder_path)
        except OSError:
            pass
    else:
        # Only delete files directly in the folder
        for name in os.listdir(folder_path):
            path = os.path.join(folder_path, name)
            if os.path.isfile(path):
                secure_delete_file(path, passes)
        try:
            os.rmdir(folder_path)
        except OSError:
            pass

def main():
    parser = argparse.ArgumentParser(description="Secure deletion tool - rewrite before delete")
    parser.add_argument("path", help="File or folder to securely delete")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively delete folders")
    parser.add_argument("-p", "--passes", type=int, default=3, help="Number of overwrite passes (default=3)")
    args = parser.parse_args()

    if os.path.isfile(args.path):
        secure_delete_file(args.path, args.passes)
    elif os.path.isdir(args.path):
        secure_delete_folder(args.path, recursive=args.recursive, passes=args.passes)
    else:
        print("[!] Path does not exist.")

if __name__ == "__main__":
    main()
