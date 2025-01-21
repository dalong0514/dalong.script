# -*- coding: utf-8 -*-
import time, re

def merge_lines(text: str) -> str:
    """
    用简单的正则把单行换行替换为空格，连续空行保留为段落。
    你可以根据需要再改得更复杂些，比如处理连字符等。
    """
    # 先将 \r\n 统一变成 \n
    text = text.replace('\r\n', '\n')
    
    # 连续2个以上换行视为段落分隔，用一个特殊标记<PARA>占位
    text = re.sub(r'\n\s*\n+', '<PARA>', text)

    # 剩下的单个换行当作同段落内换行，替换成空格
    text = re.sub(r'\n+', ' ', text)

    # 再把<PARA>还原成真正的段落分隔（这里用两个换行）
    text = text.replace('<PARA>', '\n\n')

    return text

def modify_single_file_content():
    file_name = "/Users/Daglas/Desktop/暂存数据.md"
    with open(file_name, encoding='UTF-8') as file_obj:
        content = file_obj.read()
        merged_content = merge_lines(content)
    with open(file_name, 'w', encoding='UTF-8') as file_obj:
        file_obj.write(merged_content)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    modify_single_file_content()
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')