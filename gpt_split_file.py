# -*- coding: utf-8 -*-
import glob, os, time
import modify as md

# 剔除每行开始的所有空字符串
def remove_starting_spaces(chunk):
    lines = chunk.split('\n')
    trimmed_lines = [line.lstrip() for line in lines]
    return '\n'.join(trimmed_lines)

def remove_starting_frist_space(chunk):
    lines = chunk.split('\n')
    trimmed_lines = [line[1:] if line.startswith(" ") else line for line in lines]
    return '\n'.join(trimmed_lines)

def split_txt_into_md_files(input_strings, txt_file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(txt_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 提取文件名前缀
    file_prefix = os.path.splitext(os.path.basename(txt_file_path))[0]

    split_points = [0]
    for string in input_strings:
        split_points.extend([i for i in range(len(content)) if content.startswith(string, i)])

    split_points.sort()

    for i in range(len(split_points)):
        start = split_points[i]
        end = split_points[i + 1] if i + 1 < len(split_points) else len(content)
        chunk = content[start:end]
        # 对字符串进行处理
        chunk = md.modify_text(chunk)
        # 剔除每行首个空字符串
        chunk = remove_starting_frist_space(chunk)


        # 生成文件名
        md_file_name = f"{file_prefix}{(i * 100) + 1:04d}.md"

        with open(f"{output_dir}/{md_file_name}", "w", encoding="utf-8") as output_file:
            output_file.write(chunk)

if __name__ == '__main__':
    input_strings = [
        '第1章　管理层的角色 ',
        '第2章　管理层的职责 ',
        '第3章　管理层面临的挑战 ',
        '第4章　西尔斯公司的故事',
        '第5章　企业是什么',
        '第6章　我们的事业是什么──我们的事业应该是什么',
        '第7章　企业的目标',
        '第8章　今天的决策，明天的成果',
        '第9章　生产的原则',
        '第10章　福特的故事',
        '第11章　目标管理与自我控制',
        '第12章　管理者必须管理',
        '第13章　组织的精神',
        '第14章　首席执行官与董事会',
        '第15章　培养管理者',
        '第16章　企业需要哪一种结构',
        '第17章　建立管理结构',
        '第18章　大企业、小企业和成长中的企业',
        '第19章　IBM的故事',
        '第20章　雇佣整个人',
        '第21章　人事管理是否已告彻底失败',
        '第22章　创造巅峰绩效的组织',
        '第23章　激励员工创造最佳绩效',
        '第24章　经济层面',
        '第25章　主管',
        '第26章　专业人员',
        '第27章　管理者及其工作',
        '第28章　做决策',
        '第29章　未来的管理者',
        '结语　管理层的责任'
    ]
    txt_file_path = "/Users/Daglas/Desktop/2019267管理的实践.txt"
    output_dir = "/Users/Daglas/Desktop/output_md_files"
    time1 = time.time()
    split_txt_into_md_files(input_strings, txt_file_path, output_dir)
    time2 = time.time()
    print('OK!')
    print('Time Used: ' + str(time2 - time1) + 's')