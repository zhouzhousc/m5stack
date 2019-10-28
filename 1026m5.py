import json
import csv
import serial
import time
csv_file = open('qe.csv', 'w', encoding='utf-8', newline='')  # 追加是a+
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["ax", "ay", "az", "gx", "gy", "gz", "mx", "my", "mz", "Yaw", "Pitch", "Roll", "rate"])
ser = serial.Serial(port='com3', baudrate=115200)
data = ''
while True:
    try:
        data = ser.readline()
        data = str(data, encoding="utf-8")
        line = data.replace("'", '"')
        line = json.loads(line)
        v_list = []
        for v in line.values():
            v_list.append(v)
        csv_writer.writerow(v_list)
        print(line)
    except Exception as e:
        print(e)
        time.sleep(10)


# ser.close()