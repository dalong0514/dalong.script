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
            'wisdom about them can be better than individual wisdom',
            'technological progress by establishing a backdrop of unknown',
            'which I argue that in engineering, models are stacked many layers deep',
            'ideas are more durable than the hardware itself',
            'argue that the layers of paradigms for software are so deep',
            'I argue that technology revolutions differ from scientific revolutions',
            'which I examine the concept of information',
            'I explain what software cannot do and show that the number',
            'which I go beyond the countable world of computing and argue that',
            'argue that determinism is a property of models not of the physical world',
            'model of uncertainty about a system and not directly a model of that',
            ' analyze what is holding back technology advancement',
            'These are the main reasons I wrote this book'
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

