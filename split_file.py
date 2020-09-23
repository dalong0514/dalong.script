# -*- coding: utf-8 -*-
import glob, os
import math
import pandas as pd
import modify as md

# split the arr into N chunks
def chunks(arr, in_list):
    seq = [0]
    tips = []

    for v in in_list:
        for x in arr:
            if v in x:
                seq.append(arr.index(x)-2)  # 由于定位的行前面还有个空行，所以 -2

    for v in seq:
        if seq.index(v) < len(seq) - 1:
            tips.append(arr[v:seq[seq.index(v)+1]])
    
    tips.append(arr[seq[-1]:])
    return tips

# 获得桌上所有 md 文件名并对其进行分割，然后在 for 循环里进行处理
for infile in glob.glob("/Users/Daglas/Desktop/*.txt"):
    filename, ext = os.path.splitext(infile)

    # 读取文件
    with open(filename + ".txt") as file_obj:
        lines = file_obj.readlines()

    # 对文字处理并写入文件
    with open(filename + ".txt", 'w') as file_obj:
        for line in lines:
            if line != '\n':
                new_content = md.modify_text(line)
                file_obj.write(new_content + '\n\n')

    print(len(lines))

    # 读取文件
    with open(filename + ".txt") as file_obj:
            lines = file_obj.readlines()

    # 一定要确认传入的锚点字符在文档里是唯一的，可以直接在文档里搜索来确认
    xlsx = pd.ExcelFile('readsplit.xlsx')
    ls = pd.read_excel(xlsx, 'Sheet1')
    spdots = ls['dot'].values

    n1 = 101
    n2 = 1001

    for chunk in chunks(lines, spdots):
        if n1 < 1000:
            with open(filename + "0" + str(n1-100) + ".txt", 'w') as file_obj:
                for line in chunk:
                    if line != '\n':
                        file_obj.write(line + '\n')
            n1 += 100

        else:
            with open(filename + str(n2-100) + ".txt", 'w') as file_obj:
                for line in chunk:
                    if line != '\n':
                        file_obj.write(line + '\n')
                n2 += 100
