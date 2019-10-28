import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

c_list = ["red", "green", "blue", "red", "green", "blue", "red", "green", "blue", "red", "green", "blue", "red"]
h_list = ["ax", "ay", "az", "gx", "gy", "gz", "mx", "my", "mz", "Yaw", "Pitch", "Roll", "rate"]
# dic = dict(zip(h_list, c_list))
for i in range(13):
    d_list = []

    with open('qe.csv', 'r') as csvfile:
        # 创建一个阅读器：将f传给csv.reader
        reader = csv.reader(csvfile)
        # 使用csv的next函数，将reader传给next，将返回文件的下一行
        header_row = next(reader)

        # for index, column_header in enumerate(header_row):
        #     print(index, column_header)


        data = []
            # 遍历reader的余下的所有行（next读取了第一行，reader每次读取后将返回下一行）
        for row in reader:
            # 将字符串转换成数字
            high = float(row[i])
            data.append(high)
        #print(data)

    # 绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(data, c=str(c_list[i]))
    # 设置图形的格式
    plt.title(str(h_list[i]), fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('', fontsize=16)
    plt.tick_params(axis='both', which="major", labelsize=16)

    plt.show()
