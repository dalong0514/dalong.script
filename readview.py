# -*- coding:utf-8 -*-

import glob, os
import json

import modify as md

# 获得桌上所有 md 文件名并对其进行分割，然后在 for 循环里进行处理
for infile in glob.glob("/Users/Daglas/Desktop/*.json"):
    filename, ext = os.path.splitext(infile)

    # 读取文件，文件名「filename + ".md"」是关键
    with open(filename + ".json") as file_obj:
        dictls = json.load(fp=file_obj)
        # print(dictls[:8])

    views = []
    for reviews in sorted(dictls, key = lambda e:e.__getitem__('collect'), reverse=True):
        views.append(reviews['title'])
        views.append(reviews['author'])
        views.append(reviews['date'])
        views.append(reviews['url'])
        # views.append(reviews['collect'])
        views.append(reviews['readview'])
    
    # print(views[:4])

    # 对文字处理并写入文件
    with open(filename + ".md", 'w') as file_obj:
        for view in views:
            for line in view:
                if line != '\n':
                    # line = line.replace('\n', '')
                    line = md.modify_text(line)
                    file_obj.write(line + "\n\n")