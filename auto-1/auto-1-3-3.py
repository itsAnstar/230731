import pandas as pd
import tkinter as tk
from tkinter import filedialog

# 创建一个Tkinter窗口，但不显示出来
root = tk.Tk()
root.withdraw()

# 弹出资源管理器窗口选择Excel文件
file_path = filedialog.askopenfilename(title="选择要处理的Excel文件", filetypes=[("Excel文件", "*.xlsx *.xls")])

# 读取Excel文件
df = pd.read_excel(file_path)

# 处理日期列并保存到新的列
df['新日期列'] = pd.to_datetime(df.iloc[:, 1], format='%Y/%m/%d %H:%M:%S').dt.strftime('%m%d')

# 保存处理后的数据到源目录，命名为outputfile
output_file_path = file_path.replace('.xlsx', '_outputfile.xlsx')
df.to_excel(output_file_path, index=False)

print("处理完成，输出文件名为:", output_file_path)
