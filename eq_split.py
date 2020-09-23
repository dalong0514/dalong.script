# -*- coding: utf-8 -*-
import glob, os
import math

import modify as md

# split the arr into N chunks
def chunks(arr, m):
    n = int(math.ceil(len(arr) / float(m)))
    return [arr[i:i + n] for i in range(0, len(arr), n)]

num_split = input("Please enter the num_split: ")

# 获得桌上所有 md 文件名并对其进行分割，然后在 for 循环里进行处理
for infile in glob.glob("/Users/Daglas/Desktop/*.md"):
    filename, ext = os.path.splitext(infile)

    # 读取文件
    with open(filename + ".md") as file_obj:
            lines = file_obj.readlines()

    # 对文字处理并写入文件
    with open(filename + ".md", 'w') as file_obj:
        for line in lines:
            if line != '\n':
                new_content = md.modify_text(line)
                file_obj.write(new_content + '\n\n')

    print(len(lines))

    # 读取文件
    with open(filename + ".md") as file_obj:
            lines = file_obj.readlines()

    n1 = 101
    n2 = 1001

    for chunk in chunks(lines, num_split):
        if n1 < 1000:
            with open(filename + "0" + str(n1-100) + ".md", 'w') as file_obj:
                for line in chunk:
                    if line != '\n':
                        file_obj.write(line + '\n')
            n1 += 100

        else:
            with open(filename + str(n2-100) + ".md", 'w') as file_obj:
                for line in chunk:
                    if line != '\n':
                        file_obj.write(line + '\n')
                n2 += 100