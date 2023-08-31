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
            'Cookie':'douyin.com; device_web_cpu_core=8; device_web_memory_size=8; webcast_local_quality=null; xgplayer_user_id=622570043340; n_mh=kASMHXoZNukvRs3nJS8yevfd7UTnvW4kDI2fDqznZnE; __security_server_data_status=1; LOGIN_STATUS=1; store-region=cn-js; store-region-src=uid; passport_csrf_token=4af0c703da09e3f460087d644966f019; passport_assist_user=CkFbTzMmyVLXgyEsuDqpobh8YbzX9uL_6dKuR2wYxromySKCU2JOa2an3-Dy9ArsPaPbtn_hjBemoa-QPpSt41VXNRpICjycp1FnGp3MMykX7FdsENhUIJyobQSFfjq9YlBtomT6AD8Qk3X3N6-gwYOoMBPPnlyMmydALBN1XvYqxpIQ06C2DRiJr9ZUIgEDFVYNTQ%3D%3D; sso_uid_tt=9fe24976fa943c6b4f919d8f27f8a3c9; sso_uid_tt_ss=9fe24976fa943c6b4f919d8f27f8a3c9; toutiao_sso_user=58ee1957266150ffe0f08ea8b8a3fa9e; toutiao_sso_user_ss=58ee1957266150ffe0f08ea8b8a3fa9e; uid_tt=827c2611685b49f6d509589c8440d73e; uid_tt_ss=827c2611685b49f6d509589c8440d73e; sid_tt=36aaf66f76dc59a86404457e496a0826; sessionid=36aaf66f76dc59a86404457e496a0826; sessionid_ss=36aaf66f76dc59a86404457e496a0826; _bd_ticket_crypt_cookie=698a06ed99bc71bf80fb6cbfe7afa536; s_v_web_id=verify_lkc5rcrg_H698r18s_lcHc_4n4m_AI2d_sUwf91Bz3jYF; my_rd=1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQko1SmVsdjVpbDY0WTYzTWNiRHlET1BZQ1J1OGVyaDVlSmk3ZFNnWXZDZUU3M3l5UjNwc3FGTlEwdjArTUNhSWdZcEFoK0pSZzBBYlFSYlllZEhGU009IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ==; publish_badge_show_info=%220%2C0%2C0%2C1693072395795%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.15%7D; ttwid=1%7Cgl8oBnVz25nt36GFmV3TpZA-9dSLb4Su2qcVt58qxzw%7C1693116621%7C0e190f2bd2ead7c7767c1c9056427a6c4e06c122294131fbc6abc9168ad81160; odin_tt=204d5c928cf674bc71266d86ec20463bf1d5d67dee76b6a14257b31363133ca83345719c31415b0a5a0c6dfaa24a050e; sid_ucp_sso_v1=1.0.0-KDc4ZDYxYWVlNjFjYjI1OTE3MDhmNDE1ZTU4ZGM4OTkxMmNjZWQ2ODUKHwjH7IDF3PT7BBCs8rqnBhjaFiAMMJ6W8voFOAZA9AcaAmxmIiA1OGVlMTk1NzI2NjE1MGZmZTBmMDhlYThiOGEzZmE5ZQ; ssid_ucp_sso_v1=1.0.0-KDc4ZDYxYWVlNjFjYjI1OTE3MDhmNDE1ZTU4ZGM4OTkxMmNjZWQ2ODUKHwjH7IDF3PT7BBCs8rqnBhjaFiAMMJ6W8voFOAZA9AcaAmxmIiA1OGVlMTk1NzI2NjE1MGZmZTBmMDhlYThiOGEzZmE5ZQ; sid_guard=36aaf66f76dc59a86404457e496a0826%7C1693366573%7C5184000%7CSun%2C+29-Oct-2023+03%3A36%3A13+GMT; sid_ucp_v1=1.0.0-KDM5YWUwNDU0OWFmYTZlY2M5OTdmZTFjZDUxMWZlYzhkZWVmNmRkNjEKGwjH7IDF3PT7BBCt8rqnBhjaFiAMOAZA9AdIBBoCbGYiIDM2YWFmNjZmNzZkYzU5YTg2NDA0NDU3ZTQ5NmEwODI2; ssid_ucp_v1=1.0.0-KDM5YWUwNDU0OWFmYTZlY2M5OTdmZTFjZDUxMWZlYzhkZWVmNmRkNjEKGwjH7IDF3PT7BBCt8rqnBhjaFiAMOAZA9AdIBBoCbGYiIDM2YWFmNjZmNzZkYzU5YTg2NDA0NDU3ZTQ5NmEwODI2; download_guide=%222%2F20230830%2F0%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAKuDsCszu7szRCM4dgGhBV_KSmycFL-H_7lX-78CtxKDHwRgImc-Npb3lJWI-GEa7%2F1693411200000%2F0%2F1693376820330%2F0%22; __ac_nonce=064f0103200f340429038; __ac_signature=_02B4Z6wo00f01lfLwMwAAIDBeSg6D-PbsbJX68RAAPERJYhGiyqmNOfFXfGEwFZaq71vff5z-FHmmD-IE7cJSYTOSSK12OuwnUJvMJHIjM8SZkjNwPqFL1uRZKOUBEsTXdmDguCsCFnn0.X969; home_can_add_dy_2_desktop=%220%22; strategyABtestKey=%221693454388.449%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAKuDsCszu7szRCM4dgGhBV_KSmycFL-H_7lX-78CtxKDHwRgImc-Npb3lJWI-GEa7%2F1693497600000%2F0%2F1693454388626%2F0%22; msToken=v8StJ2MMofErk74MU3j3LMP0PFs8cwkdqc0nB5QyquOFbOm2HA4jrZTMVU07ustSLgz4a-oz9TvJ4Y-KDfbkxAFvGQCHMWQR77a2d-U2dA1OkBnFPdSwRA==; msToken=mDlhAANTfqesOkF_E8Aw0peD6fzQbxavNcV8gc3xo8ZQNFQeRE2AcsY1XMYZvpLjdbGjBnTSWi_Inc2KfRa5GTQJYultKuBfNtgqaujPNYuWnL_j0vlXWA==; csrf_session_id=46f50c08e6120ef0950a822c6b123a80; tt_scid=nz3OFSYNbdp6zIoUMjubKzQk0vbo16sex774FtKku7fsLQ0dUHWfdz611Pa5JMat8798; IsDouyinActive=false; passport_fe_beating_status=false',
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
