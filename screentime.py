from __future__ import print_function
from desktopmagic.screengrab_win32 import (getScreenAsImage, getDisplaysAsImages)
from os import listdir
from os.path import isfile, join
import time
import threading

PATH = 'D:/Temp/ScreenTime/'
FFMPEG = ""
VOUTPUT = "Daily"
INC = 1
EXT = '.png'
INTERVAL = 5
END = 0

def screenshot():
     getScreenAsImage().save(PATH+VOUTPUT+str(INC)+EXT)

def start():
    global END
    global INC
    while True:
        screenshot()
        INC += 1
        time.sleep(INTERVAL)
        if END==True:
            exit()

def endInput():
    global END
    input('Press any key to stop screen capture \n')
    END=True


def appendScreenshot():
    images = [f for f in listdir(PATH) if isfile(join(PATH, f)) and f.endswith(EXT)]
    for image in images:
        pass


if __name__ == "__main__":
    begin_capture = threading.Thread(target=start)
    end_capture = threading.Thread(target=endInput)
    append_capture = threading.Thread(target=appendScreenshot)
    begin_capture.start()
    end_capture.start()


