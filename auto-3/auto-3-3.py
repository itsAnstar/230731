import os
import requests
import openpyxl
import tkinter as tk
from tkinter import filedialog


# 获取用户选择的Excel文件
root = tk.Tk()
root.withdraw()  # 隐藏主窗口
excel_file = filedialog.askopenfilename(title="选择目标Excel文件", filetypes=[("Excel Files", "*.xlsx")])
root.destroy()  # 关闭隐藏的主窗口

if not excel_file:
    print("用户取消选择Excel文件！")
else:
    # 获取用户选择的保存目录
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    save_dir = filedialog.askdirectory(title="选择保存目录")
    root.destroy()  # 关闭隐藏的主窗口

    if not save_dir:
        print("用户取消选择保存目录！")
    else:
        # 打开Excel文件
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

        # 遍历Excel表格，从第二行开始读取视频链接并下载
        for row in sheet.iter_rows(min_row=2, values_only=True):
            video_url = row[3]
            video_info = row[1] + "_" + row[2]  # 第二列和第三列的信息作为重命名的一部分

            response = requests.get(video_url)

            if response.status_code == 200:
                video_path = os.path.join(save_dir, f"{video_info}.mp4")
                with open(video_path, "wb") as f:
                    f.write(response.content)
                print(f"视频下载成功！保存路径：{video_path}")
            else:
                print("视频下载失败！")

        # 关闭Excel文件
        workbook.close()
