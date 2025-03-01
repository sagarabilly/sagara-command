# Sagara-Command

This repository is a collection of simple tools and commands that can be run easily via terminal.  
I use these commands quite often and are quite useful for both work or daily usage just to enhance productivity, setting up your pc, etc.  

## Features  
- **Sagaracrypt:** Command tools to encrypt, decrypt, file hashing and more.  
- **Sagara Wallpaper (sw):** Quickly change your desktop wallpaper with a simple command.  
- **Program Requirement Checker (prc):** An automation script that checks the installation of all programs 
- **System Monitor (sysmon):** Quickly dsplay your system status: memory, cpu, disk, boot uptime, and more.  
- **Sagara Rename (srename):** Quicky rename all the files based on a list or csv or text or even mimicking other folder.  
- **Install Engine Setup (ies) [Still under development!]:** Automation powershell script to install and setup some programs automatically. 
- **Sagara Webnote (webnote):** Displaying ypur markdown text note in a form of html with my pre-applied css design and deploy it locally (currently set to port 9995)

## Requirements  

Before using, please make sure:
- You are running Windows 10 or more. These commands are intended for Windows operating system. if you are running Windows 10, make sure you have winget installed in your system for ies command. Although, I dont recommend to use it just yet, since it is still currently being developed.  
- You have python installed on your system. it is required for sagaracrypt, sw, sysmon, and srename. All the modules used are python base modules except for srename. You need to install pandas by running ```pip install pandas``` on your system.  
All other python modules should already be already installed along with the python base installation.   
- For the use of webnote, you have to have Pandoc installed on your system [https://pandoc.org/](https://pandoc.org/)  

## Setup / Installation  

You only have to download this repository manually or clone by:   
```bash
git clone https://github.com/sagarabilly/sagara-command.git
```
And add the bin folder path to your system or user path environment variables.  

If you dont know how to add it, follow these steps:  
1. Press Win + R key on your keyboard and type ```sysdm.cpl```, and hit Ok.    
2. Head over to "Advanced" tab and click "Environmnet Variables"  
3. Click the "Path" at variable column on your user variables or system variables (depending on your choice whether to use it for all user or just for you) and click "Edit".  
4. Click "New", and add the bin folder path and hit OK.  
5. relaunch your terminal or cmd,  and it should be good to go. You can confirm it by entering command "where" followed by the command. example: ```where sw``` and it should display where the 

## Contributing
Of course, feel free to modify and any contributions are appreciated.  

