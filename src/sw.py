import os
import sys
import ctypes
import argparse
import configparser

def load_config(config_file="sw_config.ini"):
    config = configparser.ConfigParser()
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the config file: one directory up, then into the 'config' folder
    config_path = os.path.abspath(os.path.join(script_dir, "..", "config", config_file))

    if not os.path.exists(config_path):
        print(f"Configuration file {config_path} not found.")
        sys.exit(1)

    config.read(config_path)
    return config

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
    )


def get_wallpaper_path(folder_name, index, base_folder):
    if not os.path.exists(base_folder):
        print(f"Folder {base_folder} does not exist.")
        return None
    target_folder = os.path.join(base_folder, folder_name)
    if not os.path.exists(target_folder):
        print(f"Folder {target_folder} does not exist.")
        return None
    files = sorted(os.listdir(target_folder))
    if index < 1 or index > len(files):
        print(f"Invalid index. The folder has {len(files)} wallpapers.")
        return None
    return os.path.join(target_folder, files[index - 1])


def get_current_wallpaper():
    SPI_GETDESKWALLPAPER = 0x0014
    MAX_PATH = 260
    buffer = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_GETDESKWALLPAPER, MAX_PATH, buffer, 0
    )
    return buffer.value


def show_status(base_folder, folder_options):
    print("Current wallpaper status:")
    for long_flag, (folder, short_flag) in folder_options.items():
        target_folder = os.path.join(base_folder, folder)
        if os.path.exists(target_folder):
            files = sorted(os.listdir(target_folder))
            print(
                f"{folder.capitalize()} ({long_flag}/{short_flag}) folder has {len(files)} images."
            )
        else:
            print(f"{folder.capitalize()} folder does not exist.")
    print(f"Currently displaying: {get_current_wallpaper()}")


def main():
    config = load_config()
    base_folder = config.get("Settings", "folder_path", fallback=None)
    if base_folder is None:
        print("No folder_path specified in configuration.")
        sys.exit(1)

    if "Folders" not in config:
        print("Configuration missing [Folders] section.")
        sys.exit(1)

    # This dictionary will hold our folder options.
    # Key: long flag name; Value: tuple (folder_name, short_flag)
    folder_options = {}

    parser = argparse.ArgumentParser(
        description="SW - Sagara Wallpaper. Change your wallpaper via the command line."
    )
    parser.add_argument(
        "-s",
        "--status",
        action="store_true",
        help="Show the current status of wallpapers",
    )

    # Dynamically add arguments based on the configuration.
    for long_flag, value in config["Folders"].items():
        if "," in value:
            folder_name, short_flag = value.split(",", 1)
            folder_name = folder_name.strip()
            short_flag = short_flag.strip()
        else:
            folder_name = value.strip()
            short_flag = None

        folder_options[long_flag] = (folder_name, short_flag if short_flag else "")

        # Build a list of flags; always include the long flag.
        arg_flags = [f"--{long_flag}"]
        if short_flag:
            arg_flags.append(short_flag)
        parser.add_argument(
            *arg_flags, type=int, help=f"Change wallpaper for {folder_name} folder"
        )

    args = parser.parse_args()

    if args.status:
        show_status(base_folder, folder_options)
        sys.exit(0)

    # Determine which folder flag was provided.
    selected_folder = None
    index = None
    for long_flag, (folder, short_flag) in folder_options.items():
        if getattr(args, long_flag) is not None:
            selected_folder = folder
            index = getattr(args, long_flag)
            break

    if selected_folder is None:
        print("Please specify a valid folder option with its corresponding index.")
        sys.exit(1)

    wallpaper_path = get_wallpaper_path(selected_folder, index, base_folder)
    if wallpaper_path:
        print(f"Setting wallpaper: {wallpaper_path}")
        set_wallpaper(wallpaper_path)
    else:
        print("Could not set wallpaper.")


if __name__ == "__main__":
    main()
