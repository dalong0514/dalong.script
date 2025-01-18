# -*- coding: utf-8 -*-
import time, os, re
import argparse 
import pymupdf4llm


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

def get_output_dir(pdf_path):
    file_name = os.path.basename(pdf_path)
    name_without_extension = os.path.splitext(file_name)[0]
    return '/Users/Daglas/Downloads/' + name_without_extension

def pymupdf2txt(pdf_path):
    output_dir = get_output_dir(pdf_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, 'output.md')
    output_text = pymupdf4llm.to_markdown(pdf_path)
    output_text = merge_lines(output_text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_text)

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="PDF to Text Conversion using pymupdf4llm")
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    start_time = time.time()
    print('waiting...\n')
    pymupdf2txt(args.pdf_path)
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')