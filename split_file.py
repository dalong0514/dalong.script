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
    spdots = [
        'Practical Vim is for programmers who want to raise their game',
        'I demonstrate by showing examples rather than by describing them',
        'making the same small change in several places or moving around',
        'If this chapter seems surprisingly short',
        'see that there is a convenient shortcut for pasting text from a register',
        'Visual mode allows us to define a selection of text and then',
        'which is where the modal editing paradigm was conceived',
        'The buffer list lets us keep track of the set of files that',
        'which can be used to open any file by providing a filepath',
        'moving around within a document as well as commands for jumping between buffers',
        'except that they can also move us between different files',
        'and paste functionality differs from what you may be used to',
        'But when we want to repeat anything more substantial',
        'regular expressions work or how to turn them off',
        'see how we can put them to use with the search command',
        'You might think that the substitute command is just for simple',
        'runs an Ex command on each line that matches a specified pattern',
        'ctags is an external program that scans through a codebase and',
        'list is a core feature that allows us to integrate external tools into our workflow',
        'search command is great for finding all occurrences of a pattern within a file',
        'Autocompletion saves us from typing out entire words',
        'find out how to operate the spell checker from Normal mode',
        'Make it your goal to operate Vim without having to think about what',
        'The focus of this book is on mastering the core functionality of Vim'
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
