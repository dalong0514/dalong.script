import time
from gptpdf import parse_pdf
import api_key as api

# base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
# api_key = api.qwen_api_key()
api_key = api.openai_api_key()
out_filename = '/Users/Daglas/Desktop/gpt_pdf'
pdf_path = '/Users/Daglas/Dropbox/zotero/storage/DIVWD5C4/Language Models are Unsupervised Multitask Learners.pdf'

def gpt_pdf2txt():
    content, image_paths = parse_pdf(pdf_path, 
                                     output_dir=out_filename, 
                                     model="gpt-4o",
                                     api_key=api_key)
    print(content)

# def gpt_pdf2txt():
#     content, image_paths = parse_pdf(pdf_path, 
#                                      output_dir=out_filename, 
#                                      base_url = base_url,
#                                      model="qwen-vl-max",
#                                      api_key=api_key)
#     print(content)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    gpt_pdf2txt()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')