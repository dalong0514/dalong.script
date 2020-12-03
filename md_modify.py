# -*- coding:utf-8 -*-

import glob, os, time
import modify as md

def modify_file_content():
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
                    new_content = md.modify_text(line)
                    file_obj.write(new_content + "\n\n")

if __name__ == '__main__':
    start_time = time.time()
    modify_file_content()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')