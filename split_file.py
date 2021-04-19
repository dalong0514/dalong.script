# -*- coding: utf-8 -*-
import glob, os, time
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

def SplitFiles():
    # 获得桌上所有 txt 文件名并对其进行分割，然后在 for 循环里进行处理
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
        spdots = [
            'is known as a programming framework that lets developers build',
            'we often forget how lucky we are to work in an industry where',
            'Building an app is a journey of creating an initial skeleton of the app and',
            'seeing it through to the end is not so easy',
            'demoed by Ryan Dahl at JSConf in Berlin',
            'different approaches to how they function under the hood',
            'one of the first considerations is how the user will',
            'They also focus on being accessible to the user without having',
            'with using Microsoft Office will know how much functionality is available',
            'The UI of an app is one of the most important things to get right',
            'your computer and used to chat with friends and family',
            'or configuring settings for how you use a particular app',
            'Copying data from one source and using it in another is a function',
            'shortcuts is invaluable for using apps in a fast and productive manner',
            'open and running while focusing on one app at a time',
            'trace that reports what error occurred and where it happened in the code',
            'next step is to consider how you want to package it for running on your',
            'and Electron space that simplify turning built Linux executables'
        ]

        n1 = 101
        n2 = 1001

        for chunk in chunks(lines, spdots):
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

if __name__ == '__main__':
    time1=time.time()
    SplitFiles()
    time2 = time.time()
    print('OK!')
    print('Time Used: ' + str(time2 - time1) + 's')

