import pandas as pd
import datetime
from tkinter import filedialog
import tkinter as tk

def get_input_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel Files", "*.xlsx")])
    return file_path

def process_excel_file(input_file):
    # 1. 读取Excel
    df = pd.read_excel(input_file)

    # 2. 按第4列扩展选定区域倒序
    df.sort_values(by=df.columns[3], ascending=False, inplace=True)

    # 3. 删除指定列
    columns_to_drop = [df.columns[0], df.columns[1], df.columns[5], df.columns[7], df.columns[8],
                       df.columns[9], df.columns[10], df.columns[11]]
    df.drop(columns=columns_to_drop, inplace=True)

    # 4. 删除第4列中内容为"0"的行
    df = df[df[df.columns[3]] != "0"]

    # 5. 保留前100行
    df = df.head(100)

    # 4. 删除第4列
    df.drop(columns=df.columns[3], inplace=True)

    # 6. 退出并保存文件更改，并重命名文件
    today_date = datetime.datetime.now().strftime("%m%d")
    output_file = f"video{today_date}.xlsx"
    df.to_excel(output_file, index=False)

    print(f"处理完成，保存到文件: {output_file}")

if __name__ == "__main__":
    input_file_path = get_input_file_path()
    if input_file_path:
        process_excel_file(input_file_path)
