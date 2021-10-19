# -*- coding:utf-8 -*-

import glob, os, time
import modify as md


def modify_file_content():
    # 获得桌上所有 md 文件名并对其进行分割，然后在 for 循环里进行处理
    fir_dir = "/Users/Daglas/Desktop/*.md"
    # fir_dir = "C:\\Users\\dell\\Desktop\\mdFiles\\*.md"

    for infile in glob.glob(fir_dir):
        file_name, ext = os.path.splitext(infile)
        # 读取文件，文件名「file_name + ".md"」是关键
        with open(file_name + ".md", encoding='UTF-8') as file_obj:
            lines = file_obj.readlines()
        # 对文字处理并写入文件
        with open(file_name + ".md", 'w', encoding='UTF-8') as file_obj:
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