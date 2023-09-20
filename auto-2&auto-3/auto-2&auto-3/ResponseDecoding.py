import json
import requests
import re
from pprint import pprint

url = 'https://www.douyin.com/video/7274920292923788559'

# 在站点获取headers信息
headers = {
    'accept-encoding': 'deflate',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    'Sec-Fetch-Dest': 'video',
    'cookie': 'douyin.com; device_web_cpu_core=8; device_web_memory_size=8; webcast_local_quality=null; __ac_nonce=06504a9ed00fe325697a9; __ac_signature=_02B4Z6wo00f01fAMhlAAAIDCoHvCqbbRReXwLILAABkJ88; ttwid=1%7CJm-y7EiCLktRcUR4RUDELogacF1gmyyzWUEqAKYRMtM%7C1694804461%7C8c66765d2f95ae546cd6475646e5d8d6b8a8f3b88a3fb65f7339fd3a28f2936c; strategyABtestKey=%221694804462.169%22; passport_csrf_token=4551f7926e5d2dced840ebda20ea786e; passport_csrf_token_default=4551f7926e5d2dced840ebda20ea786e; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; s_v_web_id=verify_lmkytgi4_CDbfbeNX_KI4h_4TBm_8iFe_o3DxJ49YgRwk; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTExiWXc1VERhVmZac29rMHZxdW1iVFBOQWIrcXpaOU8zZmlTVG1keThOOFVVODVSZjEwVmJCNERTWmNGK21lM0cvdEhzZHFuNUtWU0ZZQWFhR01hVUk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ==; ttcid=924aad96b1174c9b9139e84db0e7d35789; download_guide=%221%2F20230916%2F0%22; pwa2=%220%7C0%7C1%7C0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; home_can_add_dy_2_desktop=%221%22; msToken=Un9ZfgZR8Ep_gZkhDwz8E5EUsmYYUYXudhXShe0NmUa7zhDwYuLWhNTMmTHTYgtZm59vxvrxB4YGNJpc8b5mQ4tQhVZ_IQoOa8b7ju5xb5KfOVg8Fw==; msToken=9ejvhoBg98xETijZvksEU4m4eoOxSOkOxlF6lUmFp-LC5Hzdm2U5W93xtZujCMeyAeq_4YG7VwVdTS_JYu4EBcx8QE_tz6Z8H12n5FZ7Cu4_dkClabkCNozStzM=; tt_scid=82iNJRDU9mFcObXs2p3SRl1AnsNP0AsQO9VE5vw5XIxUkanNdFCqUBLZ8wAIcYtn39e1; IsDouyinActive=false',
}
response = requests.get(url=url, headers=headers)
# 输出响应包体
print(response.text)
# 在响应包体中匹配title视频标题
#title = re.findall('<title data-rh="true">(.*?)</title>', response.text, re.S)[0]
# 匹配视频链接json
#video_info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>', response.text)[0]
# 对json进行解码
#video_info = requests.utils.unquote(video_info)
#json_data = json.loads(video_info)
# 输出video_info的json类型
# print(type(json_data))
# 使用pprint输出标准json漂亮格式
#pprint(json_data)

"""
# 在json中匹配视频链接
video_url = 'https:' + \
            json_data['74931a6b75e09238f154ab1577c994c9']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0][
                'src']
print(title)
print(video_url)
"""
