# -*- coding:utf-8 -*-

import glob, os, time
from bs4 import BeautifulSoup


def convert_one_file(file_name):
    # Load the HTML file
    # file_path = '/mnt/data/新知卡片：画板策略.html'
    # Read the HTML file
    with open(file_name + ".html", 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract and print the text content
    text_content = soup.get_text()
    with open(file_name + ".md", 'w', encoding='UTF-8') as file_obj:
        file_obj.write(text_content)


def convert_file():
    # 获得桌上所有 md 文件名并对其进行分割，然后在 for 循环里进行处理
    fir_dir = "/Users/Daglas/Desktop/我的笔记/*.html"

    for infile in glob.glob(fir_dir):
        file_name, ext = os.path.splitext(infile)
        # 对文字处理并写入文件
        convert_one_file(file_name)


if __name__ == '__main__':
    start_time = time.time()
    convert_file()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')