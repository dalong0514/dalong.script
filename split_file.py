# -*- coding: utf-8 -*-
import glob, os, time
import modify as md


# split the arr into N chunks
def chunks(arr, split_point_list):
    seq = [0]
    tips = []

    for v in split_point_list:
        for x in arr:
            if v in x:
                seq.append(arr.index(x)-2)  # 由于定位的行前面还有个空行，所以 -2

    for v in seq:
        if seq.index(v) < len(seq) - 1:
            tips.append(arr[v:seq[seq.index(v)+1]])

    tips.append(arr[seq[-1]:])
    return tips


def split_files():
    fir_dir = "/Users/Daglas/Desktop/*.txt"
    # fir_dir = "C:\\Users\\dell\\Desktop\\mdFiles\\*.txt"
    # 获得桌上所有 txt 文件名并对其进行分割，然后在 for 循环里进行处理
    for infile in glob.glob(fir_dir):
        filename, ext = os.path.splitext(infile)

        # 读取文件
        with open(filename + ".txt", encoding='UTF-8') as file_obj:
            lines = file_obj.readlines()

        # 对文字处理并写入文件
        with open(filename + ".txt", 'w', encoding='UTF-8') as file_obj:
            for line in lines:
                if line != '\n':
                    new_content = md.modify_text(line)
                    file_obj.write(new_content + '\n\n')

        print(len(lines))

        # 读取文件
        with open(filename + ".txt", encoding='UTF-8') as file_obj:
            lines = file_obj.readlines()

        # 一定要确认传入的锚点字符在文档里是唯一的，可以直接在文档里搜索来确认
        split_point_list = [
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

        n1 = 101
        n2 = 1001

        for chunk in chunks(lines, split_point_list):
            if n1 < 1000:
                with open(filename + "0" + str(n1-100) + ".md", 'w', encoding='UTF-8') as file_obj:
                    for line in chunk:
                        if line != '\n':
                            file_obj.write(line + '\n')
                n1 += 100

            else:
                with open(filename + str(n2-100) + ".md", 'w', encoding='UTF-8') as file_obj:
                    for line in chunk:
                        if line != '\n':
                            file_obj.write(line + '\n')
                    n2 += 100


if __name__ == '__main__':
    time1 = time.time()
    split_files()
    time2 = time.time()
    print('OK!')
    print('Time Used: ' + str(time2 - time1) + 's')

