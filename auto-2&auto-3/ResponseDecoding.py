import json
import requests
import re
from pprint import pprint

url = 'https://www.douyin.com/video/7273024102460362047'

# 在站点获取headers信息
headers = {

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
# 输出响应包体
# print(response.text)
# 在响应包体中匹配title视频标题
title = re.findall('<title data-rh="true">(.*?)</title>', response.text, re.S)[0]
# 匹配视频链接json
video_info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', response.text)[0]
# 对json进行解码
video_info = requests.utils.unquote(video_info)
json_data = json.loads(video_info)
# 输出video_info的json类型
# print(type(json_data))
# 使用pprint输出标准json漂亮格式
# pprint(json_data)

# 在json中匹配视频链接
video_url = 'https:' + \
            json_data['74931a6b75e09238f154ab1577c994c9']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0][
                'src']
print(title)
print(video_url)
