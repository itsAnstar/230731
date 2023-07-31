import os
import requests
import openpyxl

# 打开Excel文件
excel_path = os.path.join(os.path.dirname(__file__), "video.xlsx")
workbook = openpyxl.load_workbook(excel_path)
sheet = workbook.active

# 遍历Excel表格，从第二行开始读取视频链接并下载
for row in sheet.iter_rows(min_row=2, values_only=True):
    video_url = row[3]
    video_info = row[1] + "_" + row[2]  # 第二列和第三列的信息作为重命名的一部分

    response = requests.get(video_url)

    if response.status_code == 200:
        download_dir = os.path.expanduser("~/Downloads/达人视频测试/")
        video_path = os.path.join(download_dir, f"{video_info}.mp4")
        with open(video_path, "wb") as f:
            f.write(response.content)
        print(f"视频下载成功！保存路径：{video_path}")
    else:
        print("视频下载失败！")

# 关闭Excel文件
workbook.close()