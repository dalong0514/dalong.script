# -*- coding:utf-8 -*-

import glob, os, time
import modify_en as md

def modify_single_file_content():
    file_name = "/Users/Daglas/Desktop/暂存数据.md"
    with open(file_name, encoding='UTF-8') as file_obj:
        lines = file_obj.readlines()
    # 对文字处理并写入文件
    with open(file_name, 'w', encoding='UTF-8') as file_obj:
        for line in lines:
            if line != '\n':
                new_content = md.modify_text(line)
                file_obj.write(new_content + "\n\n")

if __name__ == '__main__':
    start_time = time.time()
    modify_single_file_content()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')