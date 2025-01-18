import re, time
from pathlib import Path
from html2text import html2text


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

def convert_html_to_md(input_dir):
    """
    批量将指定目录下的所有HTML文件转换为Markdown文件，
    并在转换后的MD文件第一行添加文件名
    
    Args:
        input_dir (str): 输入目录的路径
    """
    # 确保输入路径存在
    input_path = Path(input_dir)
    if not input_path.exists():
        print(f"错误：目录 '{input_dir}' 不存在")
        return

    # 获取所有html文件
    html_files = list(input_path.glob('**/*.html'))
    
    if not html_files:
        print(f"在 '{input_dir}' 目录下没有找到HTML文件")
        return
    
    print(f"找到 {len(html_files)} 个HTML文件")
    
    # 转换每个文件
    for html_file in html_files:
        # 创建输出文件路径（保持相同路径，仅改变扩展名）
        md_file = html_file.with_suffix('.md')
        # 获取不带扩展名的文件名
        file_name = html_file.stem
        
        print(f"正在转换: {html_file.name}")
        
        try:
            # 读取HTML文件内容
            with open(html_file, 'r', encoding='utf-8') as html_file_obj:
                html_content = html_file_obj.read()
            
            # 使用html2text进行转换
            md_content = html2text(html_content)
            md_content = merge_lines(md_content)
            
            # 写入最终文件，添加文件名作为第一行
            with open(md_file, 'w', encoding='utf-8') as md_file_obj:
                md_file_obj.write(f"##{file_name}\n\n{md_content}")
            
            print(f"转换成功: {md_file.name}")
            
        except Exception as e:
            print(f"处理 {html_file.name} 时发生错误: {str(e)}")

if __name__ == "__main__":
    input_directory = "/Users/Daglas/Desktop/我的笔记"
    start_time = time.time()
    print('waiting...\n')
    convert_html_to_md(input_directory)
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')