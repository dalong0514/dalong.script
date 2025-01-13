# -*- coding: utf-8 -*-
import time, os
import argparse 
from ollama_ocr import OCRProcessor

def ollama_pdf2txt(pdf_path, model_name):
    # Initialize OCR processor
    ocr = OCRProcessor(model_name, max_workers=4)  # max workers for parallel processing
    # Process multiple images
    # Process multiple images with progress tracking
    batch_results = ocr.process_batch(
        input_path=pdf_path,  # Directory or list of image paths
        format_type="markdown",
        recursive=True,  # Search subdirectories
        preprocess=True  # Enable image preprocessing
    )
    # Access results
    for file_path, text in batch_results['results'].items():
        print(f"\nFile: {file_path}")
        print(f"Extracted Text: {text}")

    # View statistics
    print("\nProcessing Statistics:")
    print(f"Total images: {batch_results['statistics']['total']}")
    print(f"Successfully processed: {batch_results['statistics']['successful']}")
    print(f"Failed: {batch_results['statistics']['failed']}")

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="PDF to Text Conversion using GPT")
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    parser.add_argument('--model', type=str, 
                       default='llama3.2-vision:11b',
                       help='GPT model to use (default: gpt-4o)')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    start_time = time.time()
    print('waiting...\n')
    ollama_pdf2txt(args.pdf_path, args.model)
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')