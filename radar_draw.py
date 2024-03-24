# -*- coding:utf-8 -*-

import time
import numpy as np
import matplotlib.pyplot as plt

# 配置matplotlib支持中文显示
plt.rcParams['font.family'] = 'Heiti TC'  # 替换为你选择的字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

def draw_radar():
    # # 轴的名称
    # categories = ['人均出图量', '数智设计用户使用率', '数智设计图纸渗透率', '数智设计项目覆盖率']
    # # 第一组值（通常在0到1之间）
    # values = [0.6, 0.7, 0.3, 0.5]
    # # 第二组值
    # values2 = [0.8, 0.9, 0.5, 0.8]
    # # 新增的第三组值
    # values3 = [0.4, 0.4, 0.2, 0.3]

    # 轴的名称
    categories = ['人均出图量', '数智设计用户使用率', '数智设计图纸渗透率']
    # 第一组值（通常在0到1之间）
    values = [0.6, 0.7, 0.3]
    # 第二组值
    values2 = [0.8, 0.9, 0.5]
    # 新增的第三组值
    values3 = [0.4, 0.4, 0.2]

    # 计算每个轴的角度
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

    # 为了使雷达图闭环，需要将第一个值添加到值列表的末尾
    values = np.concatenate((values, [values[0]]))
    values2 = np.concatenate((values2, [values2[0]]))
    values3 = np.concatenate((values3, [values3[0]]))
    angles += angles[:1]

    # 绘制雷达图
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    # 绘制第一组数据
    ax.fill(angles, values, color='red', alpha=0.25)
    ax.plot(angles, values, color='red', linewidth=2)
    # 绘制第二组数据
    ax.fill(angles, values2, color='blue', alpha=0.25)
    ax.plot(angles, values2, color='blue', linewidth=2)
    # 绘制新增的第三组数据
    ax.fill(angles, values3, color='green', alpha=0.25)
    ax.plot(angles, values3, color='green', linewidth=2)

    # 设置轴的标签位置，移动到圆圈外面
    label_distance = 1.05  # 调整这个值可以控制轴名称距离中心的距离
    for label, angle in zip(categories, angles[:-1]):
        ha = 'right' if np.cos(angle) < 0 else 'left'
        va = 'bottom' if np.sin(angle) > 0 else 'top'
        ax.text(angle, label_distance, label, ha=ha, va=va, fontsize=13, color='black')

    # 显示每个点的值
    # 第一组数据
    for angle, value in zip(angles[:-1], values[:-1]):
        ax.text(angle, value - 0.05, f"{value:.2f}", ha='center', va='center', fontsize=10, color='black')
    # 第二组数据
    for angle, value in zip(angles[:-1], values2[:-1]):
        ax.text(angle, value - 0.05, f"{value:.2f}", ha='center', va='center', fontsize=10, color='black')
    # 第三组数据
    for angle, value in zip(angles[:-1], values3[:-1]):
        ax.text(angle, value - 0.05, f"{value:.2f}", ha='center', va='center', fontsize=10, color='black')

    # 隐藏y轴的标签
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    # 显示图形
    plt.show()

if __name__ == '__main__':
    start_time = time.time()
    draw_radar()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')
