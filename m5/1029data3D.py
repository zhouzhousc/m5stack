#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import pymysql
from mpl_toolkits.mplot3d import Axes3D

db = pymysql.connect(host="localhost", user="root",
                     password="16888", db="csv_db", port=3306)

df = pd.read_sql_query("select * from m5db;", db)
yaw = pd.DataFrame(df, columns=['Yaw'])
pitch = pd.DataFrame(df, columns=['Pitch'])
roll = pd.DataFrame(df, columns=['Roll'])

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(yaw, pitch, roll)
ax.set_xlabel('pitch')
ax.set_ylabel('yaw')
ax.set_zlabel('roll')
ax.view_init(elev=10, azim=235)
plt.show()
