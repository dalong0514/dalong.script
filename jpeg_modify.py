# -*- coding: utf-8 -*-
import glob, os, time
from PIL import Image

def jpeg_modify():
    # 手动获取需要设置的宽度像素
    user_width = int(input("Please enter the image's width: "))
    # 获取该文件夹下所有特定文件的所有对象并分隔开来
    for infile in glob.glob("/Users/Daglas/Desktop/*.jpeg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        # 只对宽度像素大于给定值的图片进行处理
        if im.width > user_width:
            new_size = int(user_width), int(user_width*(im.height/im.width))
            im = im.resize(new_size)
            im.save(file + ".jpeg")

if __name__ == '__main__':
    time1 = time.time()
    jpeg_modify()
    time2 = time.time()
    print('OK!')
    print('Time Used: ' + str(time2 - time1) + 's')