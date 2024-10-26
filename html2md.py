import os
import subprocess
from pathlib import Path

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
            # 使用pandoc进行转换，先转换到临时文件
            temp_md_file = md_file.with_name(md_file.stem + "_temp.md")
            
            # 执行pandoc转换
            subprocess.run([
                'pandoc',
                '-f', 'html',
                '-t', 'markdown',
                '-o', str(temp_md_file),
                str(html_file)
            ], check=True)
            
            # 读取临时文件内容
            with open(temp_md_file, 'r', encoding='utf-8') as temp_file:
                content = temp_file.read()
            
            # 写入最终文件，添加文件名作为第一行
            with open(md_file, 'w', encoding='utf-8') as final_file:
                final_file.write(f"##{file_name}\n\n{content}")
            
            # 删除临时文件
            temp_md_file.unlink()
            
            print(f"转换成功: {md_file.name}")
            
        except subprocess.CalledProcessError as e:
            print(f"转换失败 {html_file.name}: {str(e)}")
        except Exception as e:
            print(f"处理 {html_file.name} 时发生错误: {str(e)}")
        finally:
            # 确保临时文件被删除
            if temp_md_file.exists():
                temp_md_file.unlink()

if __name__ == "__main__":
    input_directory = "/Users/Daglas/Desktop/我的笔记"
    convert_html_to_md(input_directory)