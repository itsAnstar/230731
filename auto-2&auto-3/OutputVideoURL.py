import json
import requests
import re
url = 'https://www.douyin.com/video/7271968816802860325'
headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
video_info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', response.text)[0]
video_info = requests.utils.unquote(video_info)
json_data = json.loads(video_info)
video_url = 'https:' + \
            json_data['74931a6b75e09238f154ab1577c994c9']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0]['src']
print(video_url)

