import json
import requests
import re
import os
from pprint import pprint

url = 'https://www.douyin.com/video/7271968816802860325'

headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
#print(response.text)
title = re.findall('<title data-rh="true">(.*?)</title>', response.text, re.S)[0]
video_info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', response.text)[0]
video_info = requests.utils.unquote(video_info)
json_data = json.loads(video_info)

#输出video_info的json类型
#print(type(json_data))
#输出标准json漂亮格式
#pprint(json_data)
#在json中匹配视频链接

video_url = 'https:' + json_data['74931a6b75e09238f154ab1577c994c9']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0]['src']
#print(title)
#print(video_url)


"""
以上是直链爬取模块
以下是视频下载模块
"""


# 获取视频
video_response = requests.get(video_url, stream=True)

# 确保响应状态为200
if video_response.status_code == 200:
    # 创建一个与标题相同的文件，将视频写入文件
    video_path = os.path.join(os.getcwd(), f"{title}.mp4")
    with open(video_path, 'wb') as f:
        for chunk in video_response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print(f"----视频成功下载---- @ {video_path}")
else:
    print("未知错误")


