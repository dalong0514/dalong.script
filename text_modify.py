# -*- coding: utf-8 -*-
import glob, os

import modify as md

# 获得桌上所有 md 文件名并对其进行分割，然后在 for 循环里进行处理
for infile in glob.glob("/Users/Daglas/Desktop/*.txt"):
    filename, ext = os.path.splitext(infile)

    # 读取文件，文件名「filename + ".md"」是关键
    with open(filename + ".txt") as file_obj:
        lines = file_obj.readlines()

    # 对文字处理并写入文件
    with open(filename + ".md", 'w') as file_obj:
        for line in lines:
            if line != '\n':
                new_content = md.modify_text(line)
                file_obj.write(new_content + '\n\n')