import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd


c_list = ["red", "green", "blue"] * 5
h_list = ["ax/mg", "ay/mg", "az/mg", "gx_deg/s", "gy_deg/s", "gz_deg/s", "mx/mG", "my/mG", "mz/mG", "Yaw", "Pitch", "Roll", "rate/Hz"]
# dic = dict(zip(h_list, c_list))
for i in range(13):
    d_list = []

    with open('C:/Users/F1336489/Desktop/m5_data.csv', 'r') as csvfile:
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
    # plt.subplot(431)
    plt.plot(data, c=str(c_list[i]))
    # 设置图形的格式
    plt.title(str(h_list[i]), fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('', fontsize=16)
    plt.tick_params(axis='both', which="major", labelsize=16)

    plt.show()
