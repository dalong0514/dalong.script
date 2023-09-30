# -*- coding: utf-8 -*-
import pangu
import re

def modify_text(line):
    """处理文字的格式"""
    # 去 \n 是转 pdf 时启用
    # line = line.replace('\n', '')
    line = pangu.spacing_text(line)
    new_line = line.replace(' “', '“')\
        .replace('” ', '”')\
        .replace('“', '「')\
        .replace('”', '」')\
        .replace('・', '·')\
        .replace('， ', '，')\
        .replace('。 ', '。')\
        .replace('’', '\'')\
        .replace('  ', ' ')
    new_line = new_line.strip()
    new_line = re.sub(r'(?<=[\u4e00-\u9fa5])\s+(?=[\u4e00-\u9fa5])', '', new_line)
    return new_line
