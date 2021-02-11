# -*- coding: utf-8 -*-
import glob, os, time
from pytube import YouTube

def down_video():
    print('download......')
    # YouTube('https://www.youtube.com/watch?v=0kns1gXLYg4&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=7').streams.first().download()
    video = YouTube('https://www.youtube.com/watch?v=0kns1gXLYg4&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=7')
    video.streams.all()

if __name__ == '__main__':
    time1 = time.time()
    down_video()
    time2 = time.time()
    print('OK!')
    print('Time Used: ' + str(time2 - time1) + 's')