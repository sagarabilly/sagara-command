
# Sagara Wallpaper

Sagara Wallpaper is a simple Python utility code that allows you to change your desktop wallpaper via the terminal.  
With a fully customizable configuration file, you can define the directory where your wallpapers are stored and assign your own short and long command-line flags for each wallpaper category.  
By this command, it is more easire to setup a Beautiful Terminal.  
For Bueatiful Terminal guide, please see the beautiful_terminal_README.md   

## Features

- **Dynamic Wallpaper Change:** Quickly change your desktop wallpaper using a command-line argument.
- **Customizable Categories:** Easily add or modify wallpaper categories by editing the configuration file.
- **Flexible Flags:** Define both long and short flags for each category to suit your preferences.
- **Status Overview:** Display the current wallpaper and the number of images available in each folder.

## Prerequisites

- **Operating System:** Windows (the script uses the Windows API via `ctypes` to change the wallpaper)
- **Python:** Python 3.x

## Setup

### Configure Your Setting
Edit the sw_config.ini file (located in "config" folder) to set your wallpaper directory and configure the folder options.  
Example sw_config.ini:  

```ini
[Settings]  
folder_path = D:\wallpaper  
  
[Folders]  
# Format: long_flag = folder_name, short_flag  
semi_realistic = semi_realistic, -sr  
anime = anime, -a  
beauty = beauty, -b  
nature = nature, -n  
fantasy = fantasy, -f  
```

- folder_path: Set this to the absolute path of your wallpaper folder.  
- Folders Section: For each wallpaper category, specify the folder name (which should be a subfolder under your folder_path) and assign a short flag. Modify or add categories as needed.  
  
Please remember that you have to add the sagara-command folder into your user or system path environment variables.  
See the main README.md on how to do it.   

### Running The Command / Usage Examples  
You can run the command in your terminal by simply:
```sw --help```  

to change the wallpaper you could type:  
```sw <your_flag_option> <wallpaper_number>``` depending on your sw_config.ini file.

to view the status you can run type:  
```sw --status```

## Contributing
Of course contributions are welcome! I know this is a simple code, so I welcome any of you to modify to make it better. 


