# -*- coding: utf-8 -*-
import time

def batch_create_readnotes():
    first_num = 35
    num = 2
    base_path = "/Users/Daglas/dalong.github/readnotes/20250101复制书籍/2025002The-Art-of-Doing-Science-and-Engineering/"
    book_name = "2025002The-Art-of-Doing-Science-and-Engineering"
    default_content = "Richard W. Hamming.(2020.1997).2025002The-Art-of-Doing-Science-and-Engineering.Stripe Press => 0101Introduction"
    
    for i in range(0, num):
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
    print('waiting...\n')
    batch_create_readnotes()
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')