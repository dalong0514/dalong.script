# -*- coding: utf-8 -*-
import glob, os

import pangu

# 手动获取需要设置的宽度像素
init_num = int(input("Please enter the init number: "))
input_format = input("Please enter the image's format(default-png): ")

if input_format != '':
    image_format = input_format
else:
    image_format = 'png'

# 获得桌上所有 md 文件名并对其进行分割，然后在 for 循环里进行处理
for infile in glob.glob("/Users/Daglas/Desktop/*.md"):
    filename, ext = os.path.splitext(infile)

    # 读取文件，文件名「filename + ".md"」是关键
    with open(filename + ".md") as file_obj:
        lines = file_obj.readlines()

    # 对文字处理并写入文件
    with open(filename + ".md", 'w') as file_obj:
        for line in lines:
            if line != '\n':
                image_path = "![](./res/" + str(init_num) + "." + image_format + ")"
                if "图图" in line:
                    line = line.replace("图图", image_path)
                    init_num += 1
                file_obj.write(line + '\n')