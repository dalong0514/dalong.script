# -*- coding:utf-8 -*-

import time
import json

import json

def extract_transcript_sequential(json_path):
    """
    从指定的 JSON 文件中按顺序提取并分组说话人的文本。
    只有相邻的同一说话人的内容会被合并，不同说话人之间用换行符隔开。

    参数:
        json_path (str): JSON 文件的路径。

    返回:
        str: 按顺序分组并拼接后的完整文稿。
    """
    try:
        # 读取 JSON 文件
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"文件未找到: {json_path}")
        return ""
    except json.JSONDecodeError:
        print(f"文件不是有效的 JSON 格式: {json_path}")
        return ""

    # 提取 'speakers' 数组
    speakers_data = data.get('speakers', [])

    if not speakers_data:
        print("JSON 文件中没有 'speakers' 数据。")
        return ""

    # 初始化
    transcript_blocks = []
    current_speaker = None
    current_text = []

    # 遍历每个说话人条目
    for entry in speakers_data:
        speaker = entry.get('speaker')
        text = entry.get('text', '').strip()

        if not speaker or not text:
            continue  # 跳过没有说话人或文本的条目

        if speaker == current_speaker:
            # 同一说话人，追加文本
            current_text.append(text)
        else:
            # 不同说话人，先保存之前的块
            if current_speaker is not None:
                block = f"{current_speaker}: {' '.join(current_text)}"
                transcript_blocks.append(block)
            # 更新当前说话人和文本
            current_speaker = speaker
            current_text = [text]

    # 添加最后一个说话人的内容
    if current_speaker is not None and current_text:
        block = f"{current_speaker}: {' '.join(current_text)}"
        transcript_blocks.append(block)

    # 使用换行符分隔不同说话人的内容
    full_transcript = "\n\n".join(transcript_blocks)

    return full_transcript

def audio_text_process():
    # JSON 文件路径
    json_path = '/Users/Daglas/Desktop/output.json'

    # 提取并生成文稿
    transcript = extract_transcript_sequential(json_path)

    if transcript:
        # 打印文稿
        # print("完整的音频文稿如下：\n")
        # print(transcript)

        # 可选：将文稿保存到文件
        output_path = '/Users/Daglas/Desktop/output.md'
        try:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(transcript)
            print(f"\n文稿已成功保存到: {output_path}")
        except IOError:
            print(f"无法写入文件: {output_path}")


if __name__ == '__main__':
    start_time = time.time()
    audio_text_process()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')
