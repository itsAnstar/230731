import os
import tkinter as tk
from datetime import datetime
from tkinter import filedialog

import pandas as pd


def get_input_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="选择Excel文件", filetypes=[("Excel文件", "*.xlsx")])
    return file_path


def get_unique_file_name(folder, base_name, extension, counter=0):
    if counter == 0:
        file_name = f"{base_name}.{extension}"
    else:
        file_name = f"{base_name}-{counter}.{extension}"
    file_path = os.path.join(folder, file_name)
    if os.path.exists(file_path):
        return get_unique_file_name(folder, base_name, extension, counter + 1)
    return file_name


def process_excel_file(input_file):
    # 1. 读取Excel文件
    df = pd.read_excel(input_file)

    # 2. 按第四列降序排序
    df.sort_values(by=df.columns[3], ascending=False, inplace=True)

    # 3. 删除指定列
    columns_to_drop = [df.columns[0], df.columns[1], df.columns[5], df.columns[7], df.columns[8],
                       df.columns[9], df.columns[10], df.columns[11]]
    df.drop(columns=columns_to_drop, inplace=True)

    # 4. 删除第四列中内容为"0"的行
    df = df[df[df.columns[3]] != "0"]

    # 5. 保留前50行
    df = df.head(50)

    # 6. 删除第四列
    df.drop(columns=df.columns[3], inplace=True)

    # 处理第二列的日期时间数据
    df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: datetime.strptime(str(x), '%Y/%m/%d %H:%M:%S').strftime('%m%d'))

    # 7. 保存修改后的文件，并使用新名称
    today_date = datetime.now().strftime("%m%d")
    base_name = f"video-{today_date}"
    folder = os.path.dirname(input_file)
    extension = "xlsx"
    output_file_name = get_unique_file_name(folder, base_name, extension)
    output_file_path = os.path.join(folder, output_file_name)
    df.to_excel(output_file_path, index=False)

    print(f"处理完成，保存到文件: {output_file_path}")


if __name__ == "__main__":
    input_file_path = get_input_file_path()
    if input_file_path:
        process_excel_file(input_file_path)
