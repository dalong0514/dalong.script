# -*- coding: utf-8 -*-
import time
import ollama

def extract_content(response):
    return response['message']['content']

def local_pdf2txt(image_path, filename):
    role = 'You are an image content interpreter, tasked with transcribing image content using markdown and LaTeX formatting.'
    prompt = """
Use markdown formatting for the entire content with these specifications:
1. Output the content directly without enclosing in markdown code blocks
2. Format equations as follows:
   - Block equations: Use $$ $$
   - Inline equations: Use $ $
3. Omit:
   - Horizontal rules
   - Page numbers
4. Provide the content directly without explanatory notes
"""
    response = ollama.chat(
        model='llama3.2-vision:90b',
        messages=[{
            'role': role,
            'content': prompt,
            'images': [image_path]
        }]
    )
    content = extract_content(response)
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + '\n')
    print(content)

if __name__ == '__main__':
    image_path = '/Users/Daglas/Desktop/0101.png'
    output_filename = '/Users/Daglas/Desktop/output.md'

    start_time = time.time()
    print('waiting...\n')
    local_pdf2txt(image_path, output_filename)
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')