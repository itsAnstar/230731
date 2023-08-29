import tkinter as tk
from tkinter import filedialog
import pandas as pd
from datetime import datetime
import os

# 创建隐藏的主窗口
root = tk.Tk()
root.withdraw()

# 打开文件选择对话框让用户选择Excel文件
file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])

# 读取用户选择的Excel文件
df = pd.read_excel(file_path)

# 删除第1、2、6列
df = df.drop(df.columns[[0, 1, 5]], axis=1)

# 第2列按照选定分区降序排序
df = df.sort_values(df.columns[1], ascending=False)

# 把第二列的数值从“2023/04/06 18:02:44”转换成MMDD格式，如“0406”
df[df.columns[1]] = pd.to_datetime(df[df.columns[1]]).dt.strftime('%m%d')

# 打印读取到的数据，每一天只输出一次
unique_dates = df[df.columns[1]].unique()
print("\n".join(unique_dates))

# 让用户输入数字选择需要保存几天的数据
num_days = int(input("请输入需要保存的天数："))

# 只保存用户选择的日期的行
selected_dates = unique_dates[:num_days]
df = df[df[df.columns[1]].isin(selected_dates)]



# 让用户输入数字选择需要保存的文件名
print("请输入需要保存的文件名：")
print("1: 糖醋排哭")
print("2: 西湖醋鱼")
print("3: 粉蒸肉")
file_name_choice = int(input())

# 根据用户的选择设置文件名
if file_name_choice == 1:
    file_name = "糖醋排骨"
elif file_name_choice == 2:
    file_name = "西湖醋鱼"
elif file_name_choice == 3:
    file_name = "粉蒸肉"
else:
    print("输入错误，将使用默认文件名")
    file_name = "default"

# 获取用户选择的文件的目录
dir_path = os.path.dirname(file_path)

# 将处理后的Excel数据保存到一个新文件
today = datetime.now().strftime('%m%d')
output_filename = os.path.join(dir_path, f"{file_name}_{today}_output.xlsx")
counter = 1
while os.path.exists(output_filename):
    output_filename = os.path.join(dir_path, f"{file_name}_{today}_output-{counter}.xlsx")
    counter += 1

df.to_excel(output_filename, index=False)

print(f"处理完成--> 输出文件路径: {os.path.abspath(output_filename)}")
