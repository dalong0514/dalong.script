# -*- coding: utf-8 -*-
import time

def batch_create_readnotes():
    first_num = 20
    num = 4
    base_path = "/Users/Daglas/dalong.GitHub/readnotes/20240101复制书籍/2024159科技群星闪耀时/"
    book_name = "2024159科技群星闪耀时"
    default_content = 'Stephen Wolfram.(2024/2016).2024159科技群星闪耀时.(应俊耀等译).人民邮电出版社 => 前言'
    
    for i in range(1, num + 1):
        # 格式化序号，确保是4位数字，前两位是批次号，后两位是01
        formatted_num = f"{first_num + i:02}01"
        file_name = f"{book_name}{formatted_num}.md"
        file_path = base_path + file_name
        
        # 创建文件并写入内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(default_content)
            
        print(f"已创建文件: {file_name}")

if __name__ == '__main__':
    start_time = time.time()
    batch_create_readnotes()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')