# -*- coding: utf-8 -*-
import pangu

def modify_text(line):
    """处理文字的格式"""
    # 去 \n 是转 pdf 时启用
    # line = line.replace('\n', '')
    line = pangu.spacing_text(line)
    line = line.replace(' “', '“')
    line = line.replace('” ', '”')
    line = line.replace('“', '「')
    line = line.replace('”', '」')
    line = line.replace('・', '·')
    line = line.replace('， ', '，')
    line = line.replace('。 ', '。')
    line = line.strip()
    return line
