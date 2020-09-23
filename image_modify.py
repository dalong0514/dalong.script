# -*- coding: utf-8 -*-
import glob, os

from PIL import Image

# 手动获取需要设置的宽度像素
user_width = int(input("Please enter the image's width: "))
# 手动获取图片的格式
image_format = input("Please enter the image's format(jpg/jpeg/png-default): ")

# if image_format != ''
#     im_format =image_format
# else:
#     im_format = 'png'

# 获取该文件夹下所有特定文件的所有对象并分隔开来
for infile in glob.glob("/Users/Daglas/Desktop/*." + image_format):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)

    # 只对宽度像素大于给定值的图片进行处理
    if im.width > user_width:
        new_size = int(user_width), int(user_width*(im.height/im.width))
        im = im.resize(new_size)
        im.save(file + "." + image_format)