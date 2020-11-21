# -*- coding: utf-8 -*-
import glob, os, time
import math
import pandas as pd
import modify as md

# split the arr into N chunks
def chunks(arr, in_list):
    seq = [0]
    tips = []

    for v in in_list:
        for x in arr:
            if v in x:
                seq.append(arr.index(x)-2)  # 由于定位的行前面还有个空行，所以 -2

    for v in seq:
        if seq.index(v) < len(seq) - 1:
            tips.append(arr[v:seq[seq.index(v)+1]])
    
    tips.append(arr[seq[-1]:])
    return tips

def SplitFiles():
    # 获得桌上所有 txt 文件名并对其进行分割，然后在 for 循环里进行处理
    for infile in glob.glob("/Users/Daglas/Desktop/*.txt"):
        filename, ext = os.path.splitext(infile)

        # 读取文件
        with open(filename + ".txt") as file_obj:
            lines = file_obj.readlines()

        # 对文字处理并写入文件
        with open(filename + ".txt", 'w') as file_obj:
            for line in lines:
                if line != '\n':
                    new_content = md.modify_text(line)
                    file_obj.write(new_content + '\n\n')

        print(len(lines))

        # 读取文件
        with open(filename + ".txt") as file_obj:
                lines = file_obj.readlines()

        # 一定要确认传入的锚点字符在文档里是唯一的，可以直接在文档里搜索来确认
        spdots = [
            '你可能读了几个月的报纸，或者看了几个月的电视新闻，却没有见过一个代数公式',
            '34个州共有超过1000家餐馆参与了这项活动，每周一会',
            '同性婚姻一直富有争议性，许多人基于宗教信仰表示反对',
            '某项民意调查访问了随机抽样的1000个人后，公布了调查结果',
            '媒体对于气候变化的报道似乎非常频繁。气候学家警告我们',
            '真的存在咖啡因依赖吗',
            '酒精是否可以增强我们对异性吸引力的感知',
            '脑容量大的人更聪明吗？为了回答这个问题',
            '该榜单在指导公众评估美国大学的质量方面非常有影响力，然而',
            '美国人的阅读量在减少，而且阅读技能在衰退',
            '营养学家告诉我们，健康的饮食习惯包括每天摄入20~35克纤维',
            '教育是否值得投资？我们了解到，一般来说',
            '柱状图和直方图自然是很古老的图形了。用柱状图来展示数据',
            '媒体有发布排名的癖好，最宜居的城市、最好的大学、最健康的食物',
            '预测股市的走势可能让你发财，难怪有那么多人都埋头在股市信息里',
            '排名前三的全垒打球员分别是巴里',
            '犹他州普罗沃一位女性连续第三次在同一日期生下婴儿',
            '就在纽约巨人队赢得第46届超级碗冠军后不久',
            '对于赛马而言，起点位置决定了最后结果。如果起点靠近内跑道',
            '如果你赌博，你就会在乎赢钱的概率有多大，它可以告诉你',
            '你认识很容易生气的人吗？大自然有办法让这些人平静下来',
            '一篇文章报道了大学新生的压力水平。造成这种情况的根本原因是',
            '假设我们查看超过10000只面向大众投资者发行的共同基金',
            '高校之一，该校的特色专业是工程学、科学与技术。在2010',
            '这些争议并没有大家一致认同的解决方法，我们的答案只包括应该纳入讨论的'
        ]

        n1 = 101
        n2 = 1001

        for chunk in chunks(lines, spdots):
            if n1 < 1000:
                with open(filename + "0" + str(n1-100) + ".md", 'w') as file_obj:
                    for line in chunk:
                        if line != '\n':
                            file_obj.write(line + '\n')
                n1 += 100

            else:
                with open(filename + str(n2-100) + ".md", 'w') as file_obj:
                    for line in chunk:
                        if line != '\n':
                            file_obj.write(line + '\n')
                    n2 += 100

if __name__ == '__main__':
    time1=time.time()
    SplitFiles()
    time2 = time.time()
    print('OK!')
    print('Time Used: ' + str(time2 - time1) + 's')

