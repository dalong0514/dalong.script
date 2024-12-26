# -*- coding: utf-8 -*-
import time, os
from gptpdf import parse_pdf
import api_key as api

api_key = api.deepseek_api_key()
base_url= 'https://api.deepseek.com/v1'
model_name='deepseek-chat'

pdf_path = '/Users/Daglas/Downloads/thatsinteresting_1971_1.pdf'

def get_out_filename():
    file_name = os.path.basename(pdf_path)
    name_without_extension = os.path.splitext(file_name)[0]
    return '/Users/Daglas/Downloads/' + name_without_extension

def gpt_pdf2txt():
    out_filename = get_out_filename()
    content, image_paths = parse_pdf(pdf_path, 
                                     output_dir=out_filename, 
                                     base_url = base_url,
                                     model=model_name,
                                     api_key=api_key)
    print(content)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    gpt_pdf2txt()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')