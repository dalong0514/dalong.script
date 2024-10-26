# -*- coding:utf-8 -*-
import glob, os, time
from PIL import Image

def convert_image(input_path, output_format):
    try:
        with Image.open(input_path) as img:
            file_name, _ = os.path.splitext(input_path)
            output_path = f"{file_name}.{output_format.lower()}"
            # 如果输入图片模式是RGBA (PNG with transparency),
            # 转换为RGB模式 (因为BMP不支持透明度)
            if img.mode == 'RGBA' and output_format.upper() == 'BMP':
                img = img.convert('RGB')
            
            img.save(output_path, output_format.upper())
        print(f"转换成功: {output_path}")
        return output_path
    except Exception as e:
        print(f"转换失败 {input_path}: {str(e)}")
        return None

def batch_convert_images(input_folder, output_format):
    if not os.path.exists(input_folder):
        print(f"错误: 文件夹 '{input_folder}' 不存在。")
        return

    successful_conversions = 0
    failed_conversions = 0

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_path):
            try:
                # 尝试打开文件以检查它是否为有效的图像文件
                Image.open(input_path)
                result = convert_image(input_path, output_format)
                if result:
                    successful_conversions += 1
                else:
                    failed_conversions += 1
            except IOError:
                # 如果文件不是图像,跳过它
                print(f"跳过非图像文件: {filename}")

    print(f"\n批量转换完成:")
    print(f"成功转换: {successful_conversions}")
    print(f"转换失败: {failed_conversions}")

if __name__ == '__main__':
    start_time = time.time()
    # 使用函数
    input_folder = "/Users/Daglas/Desktop"
    output_format = "BMP"  # 可以根据需要更改为 'BMP' 或其他支持的格式
    batch_convert_images(input_folder, output_format)
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')