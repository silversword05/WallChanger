# WallChanger
A python script that auto-changes your wall-paper after specific time-intervals

# How to use
Download the python file and bring it to your home folder
Set the file-path to your wall-papers folder ( An example is already there)
Set you sleep-time  (a value greater than 7 is good)

First execute the script as 
```
python3 WallChanger.py
```

If it works fine or install the requirements (os , glob , random , time). Probably all should be installed

Download the script file and provide the file-path at the 6th line

DO NOT GIVE X-GNOME-Autostart-Delay=0

Save the file as MyScript.desktop
Now move the file to /home/aadi/.config/autostart

In home folder some files are hidden, press Ctrl+H to see the hidden files, you will see .config folder
        
Then right-click on MyScript.desktop and go to properties and then go to permissions. Check-in the box "Allow executing file as program"

All Set ENJOY!!!!


# Cautions

If you add a new image in the folder, that image will be counted from your next reboot

If you delete any image, then default wallpaper will be shown in its place. It will be corrected in your next start-up

To stop this, delete the MyScript.desktop file in /home/aadi/.config/autostart and perform a restart and then the delete the wallpaper folder.

DO NOT DELETE THE WALL-PAPER FOLDER BEFORE DELETING THE AUTO-START SCRIPT. DELETE THE FOLDER AFTER THE NEXT RE-BOOT
