# -*- coding: utf-8 -*-

"""
请从alphavantage拿到微软的每日数据
然后使用pandas来进行数据处理 
最后使用matplotlib库把图表给画出来
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc", size=14)

def get_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo&datatype=csv"
    r = requests.get(url)
    with open("msft.csv", "wb") as f:
        f.write(r.content)

def draw():
    df = pd.read_csv("msft.csv")
    df = df.sort_values(by="timestamp")
    df = df.set_index("timestamp")
    df = df.drop(["open", "high", "low", "volume"], axis=1)
    df.plot()
    plt.legend(prop=font)
    plt.title("微软每日股价", fontproperties=font)
    plt.xlabel("日期", fontproperties=font)
    plt.ylabel("美元", fontproperties=font)
    plt.show()

if __name__ == "__main__":
    get_data()
    draw()

