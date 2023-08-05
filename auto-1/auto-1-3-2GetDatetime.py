import pandas as pd
import datetime
from tkinter import filedialog
import tkinter as tk
import os

def get_input_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="选择Excel文件", filetypes=[("Excel文件", "*.xlsx")])
    return file_path


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

    # 5. 保留前100行
    df = df.head(100)

    # 6. 删除第四列
    df.drop(columns=df.columns[3], inplace=True)

    # 任务1：在第二列之前插入一列，设置单元格格式为文本格式，从第三列对应单元格中提取第6、7、9、10位内容
    new_column = df[df.columns[1]]  # 获取第二列
    new_column = new_column.astype(str)  # 将新列转换为字符串类型
    new_column = new_column.str.replace('.0', '')  # 去除第一个单元格中的小数点和零
    new_column = new_column.str.zfill(2)  # 在第一个单元格中填充零，使其成为两位数
    df.insert(1, '新列', new_column)  # 在第二列之前插入新列

    for row in range(3, df.shape[0]):  # 从第三行开始遍历所有行
        cell_value = df.iloc[row, 2]  # 获取第三列对应行的值
        df.at[row, '新列'] = cell_value[-6:-4]  # 提取第6、7、9、10位内容并赋值给新列对应行单元格

       # 7. 保存修改后的文件，并使用新名称
    today_date = datetime.datetime.now().strftime("%m%d")
    output_file_name = f"video{today_date}.xlsx"
    output_file_path = os.path.join(os.path.dirname(input_file), output_file_name)
    df.to_excel(output_file_path, index=False)

    print(f"处理完成，保存到文件: {output_file_path}")

if __name__ == "__main__":
    input_file_path = get_input_file_path()
    if input_file_path:
        process_excel_file(input_file_path)