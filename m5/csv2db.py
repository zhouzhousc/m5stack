#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pymysql
import pandas as pd

# 参数设置,建立连接
db = pymysql.connect(host="localhost", user="root",
                     password="16888", db="localsql", port=3306)

# 自动确认commit True
db.autocommit(1)
# 设置光标
cursor = db.cursor()

df = pd.read_csv('qe.csv', encoding='utf-8')


# 一个根据pandas自动识别type来设定table的type
def make_table_sql(df):
    columns = df.columns.tolist()
    types = df.ftypes
    # 添加id 制动递增主键模式
    make_table = []
    char = ''
    for item in columns:
        if 'int' in types[item]:
            char = item + ' INT'
        elif 'float' in types[item]:
            char = item + ' FLOAT'
        elif 'object' in types[item]:
            char = item + ' VARCHAR(255)'
        elif 'datetime' in types[item]:
            char = item + ' DATETIME'
        make_table.append(char)
    return ','.join(make_table)


# csv 格式输入 mysql 中
def csv2mysql(db_name, table_name, df):
    # 创建database
    cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_name))
    # 选择连接database

    db.select_db(db_name)

    # 创建table
    cursor.execute('DROP TABLE IF EXISTS {}'.format(table_name))
    cursor.execute('CREATE TABLE {}({})'.format(table_name, make_table_sql(df)))

    values = df.values.tolist()
    # 根据columns个数
    s = ','.join(['%s' for _ in range(len(df.columns))])
    # executemany批量操作 插入数据 批量操作比逐个操作速度快很多
    cursor.executemany('INSERT INTO {} VALUES ({})'.format(table_name, s), values)


csv2mysql('csv_db', 'm5db', df)
# 光标关闭
cursor.close()
# 连接关闭
db.close()



