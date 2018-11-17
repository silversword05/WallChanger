import os
import glob
from random import *
import time

filepath = "/home/aadi/Pictures/wallpapers"
sleeptime = 10

filepath = filepath + "/*"

list = glob.glob(filepath)
c = len(list)

while True:
    index = randint(0,c-1)
    try:
        os.system("gsettings set org.gnome.desktop.background picture-uri file:" + list[index])
    except:
        pass
    time.sleep(sleeptime)

