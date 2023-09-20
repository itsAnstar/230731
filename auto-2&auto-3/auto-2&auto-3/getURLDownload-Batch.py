# 本文件为最终完全体
# auto-1输出的excel文件直接传递给本程序可以直接下载


import json
import requests
import re
import os
import datetime
import logging
from pprint import pprint
import pandas as pd
from tkinter import filedialog
from tkinter import Tk

# 创建一个Tkinter窗口并立即隐藏
root = Tk()
root.withdraw()

# 打开文件选择对话框，让用户选择Excel文件
file_path = filedialog.askopenfilename(title="选择excel文件")
print(f"将要遍历的Excel文件：{file_path}")

# 打开文件夹选择对话框，让用户选择目标文件夹
dest_dir = filedialog.askdirectory(title="选择保存目录")
print(f"目标存储目录：{dest_dir}")

# 使用pandas读取Excel文件
df = pd.read_excel(file_path)

# 获取当前日期
now = datetime.datetime.now()
date_str = now.strftime("%Y%m%d")

# 创建日志文件的名字
log_file_name = f"log_{date_str}.txt"
suffix = 1

# 检查目标目录是否存在同名文件，如果存在，就在文件名后面添加后缀
while os.path.exists(os.path.join(dest_dir, log_file_name)):
    log_file_name = f"log_{date_str}-{suffix}.txt"
    suffix += 1

# 创建一个日志记录器
logging.basicConfig(filename=os.path.join(dest_dir, log_file_name), level=logging.INFO)

# 记录程序开始的时间
logging.info(f"程序开始运行: {datetime.datetime.now()}")
# 增加成功计数器
success_count = 0

# 遍历Excel文件的所有行
total_rows = len(df)
for i in range(total_rows):
    # 打印行号和总行数
    print(f"正在解析第 {i + 1} 行...共{total_rows}条")
    logging.info(f"正在解析第 {i + 1} 行...共{total_rows}条")

    # 获取第一列的值，赋予给requests.get的URL参数
    url = df.iloc[i, 0]
    print(f"视频原地址: {url}")
    logging.info(f"视频原地址: {url}")

    # 获取第二列和第三列的值，用于文件命名
    file_name = str(df.iloc[i, 1]).zfill(4) + '_' + str(df.iloc[i, 2])

    try:

        headers = {
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
        # 发送请求
        response = requests.get(url=url, headers=headers)                           
        title = re.findall('<title data-rh="true">(.*?)</title>', response.text, re.S)[0]
        video_info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', response.text)[0]
        video_info = requests.utils.unquote(video_info)
        json_data = json.loads(video_info)

        video_url = 'https:' + \
                    json_data['74931a6b75e09238f154ab1577c994c9']['aweme']['detail']['video']['bitRateList'][0][
                        'playAddr'][0]['src']

        # 获取视频，设置超时时间为600秒（10分钟）
        video_response = requests.get(video_url, stream=True, timeout=600)

        # 确保响应状态为200
        if video_response.status_code == 200:
            # 创建一个与标题相同的文件，将视频写入文件
            video_path = os.path.join(dest_dir, f"{file_name}.mp4")
            with open(video_path, 'wb') as f:
                for chunk in video_response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f"----上述视频成功下载----> {video_path}")
            logging.info(f"----上述视频成功下载----> {video_path}")
            # 成功请求则success参数自加1
            success_count += 1
            print(f"--视频标题--{title}")
            logging.info(f"{title}")
            print('-------------------------------------------------------------------------------------------------------')
            logging.info('-------------------------------------------------------------------------------------------------------')
        else:
            print("\033[31m未知错误\033[0m")
    except requests.exceptions.Timeout:
        print("\033[31m请求超时，跳过这一行\033[0m")
        logging.error("请求超时，跳过这一行")
        continue
    except Exception as e:
        print("\033[31m上述视频下载失败-->视频已被删除或隐藏\033[0m")
        logging.error(f"上述视频下载失败-->视频已被删除或隐藏, 错误详情: {e}")
        print(f"错误详情: {e}")
        logging.error(f"错误详情: {e}")
        print('-------------------------------------------------------------------------------------------------------')
        continue
# 记录程序结束的时间
logging.info(f"程序结束运行: {datetime.datetime.now()}")

# 打印运行总结
print("-------------------------------------------------------------------------------------------------------")
print(f"-----所有视频下载完成--->本次遍历共{total_rows}条视频--->成功下载{success_count}条视频----")
print("-------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------")
logging.info(f"----所有视频下载完成----本次遍历共{total_rows}条视频，成功下载{success_count}条视频----")

# 等待用户输入
input("按任意键结束程序...")
