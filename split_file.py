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
            'This book is concerned with the nuts and bolts of manipulating',
            'When I wrote the first edition of this book in 2011 and 2012',
            'This chapter discusses capabilities built into the Python language that will',
            'array objects as the lingua franca for data exchange',
            'pandas will be a major tool of interest throughout much of the rest of the book',
            'Accessing data is a necessary first step for using most of the tools in this book',
            'During the course of doing data analysis and modeling',
            'data may be spread across a number of files or databases or',
            'to help identify outliers or needed data transformations',
            'Categorizing a dataset and applying a function to each group',
            'Time series data is an important form of structured data in many different fields',
            'The preceding chapters have focused on introducing different types of data',
            'I have focused on providing a programming foundation for doing data',
            'contains a collection of miscellaneous example datasets that you can use',
            'I will go deeper into the NumPy library for array computing',
            'we looked at the basics of using the IPython shell and Jupyter notebook'
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

