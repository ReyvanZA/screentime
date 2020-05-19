from os import listdir, system
from os.path import isfile, join
import os.path
import ffmpeg

PATH = 'D:/Temp/ScreenTime/'
EXT = '.png'

images = [f for f in listdir(PATH) if isfile(join(PATH, f)) and f.endswith(EXT)]
videoFiles = []

for image in images:
    system('ffmpeg -y -framerate 24 -loop 1 -t 2 -i '+ PATH + image + ' '+ image.split('.')[0] +'.mpg')
    videoFiles.append(image.split('.')[0] + '.mpg')

videoTxt = '|'
videoTxt = videoTxt.join(videoFiles)

videoTxt = 'concat:' + videoTxt

system('ffmpeg -y -r 2 -i "'+ videoTxt +'" -c copy output.mpg')





