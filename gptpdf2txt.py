import time
from gptpdf import parse_pdf
import api_key as api

api_key = api.openai_api_key()
out_filename = '/Users/Daglas/Desktop/gpt_pdf'
pdf_path = '/Users/Daglas/Dropbox/zotero/storage/4VEHQZ9S/Vaswani et al_2023_Attention Is All You Need.pdf'

def gpt_pdf2txt():
    content, image_paths = parse_pdf(pdf_path, 
                                     out_filename=out_filename, 
                                     api_key=api_key)
    print(content)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    gpt_pdf2txt()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')