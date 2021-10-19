# -*- coding: utf-8 -*-
import pangu


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
    return new_line
