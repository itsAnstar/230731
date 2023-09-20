import requests
import json
import re
from pprint import pprint
headers = {
    'Cookie': 'douyin.com; device_web_cpu_core=8; device_web_memory_size=8; webcast_local_quality=null; ttwid=1%7CJm-y7EiCLktRcUR4RUDELogacF1gmyyzWUEqAKYRMtM%7C1694804461%7C8c66765d2f95ae546cd6475646e5d8d6b8a8f3b88a3fb65f7339fd3a28f2936c; passport_csrf_token=4551f7926e5d2dced840ebda20ea786e; passport_csrf_token_default=4551f7926e5d2dced840ebda20ea786e; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; s_v_web_id=verify_lmkytgi4_CDbfbeNX_KI4h_4TBm_8iFe_o3DxJ49YgRwk; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTExiWXc1VERhVmZac29rMHZxdW1iVFBOQWIrcXpaOU8zZmlTVG1keThOOFVVODVSZjEwVmJCNERTWmNGK21lM0cvdEhzZHFuNUtWU0ZZQWFhR01hVUk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ==; ttcid=924aad96b1174c9b9139e84db0e7d35789; download_guide=%223%2F20230916%2F0%22; pwa2=%220%7C0%7C3%7C0%22; __ac_nonce=0650b310f00a595346dbc; __ac_signature=_02B4Z6wo00f01hCH8twAAIDBQPC2JghftaoQp.ZAAOE43EoSXaNEu7ZzygKGgL2CgLOqZeyZMwZoyIYeu1hL5kQFMn.yBgr.ubFBo3nPNhfpqyagIuZRkUDSRxvc5AHsfgtqT3U6mek2pjEa8c; strategyABtestKey=%221695232272.512%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; home_can_add_dy_2_desktop=%221%22; msToken=uulo0c4NiDDw5MxDaGuIQ6xltI3BG9NYkG1X8oz00NOELOxn2m7lobbd4W7aUmX6LNk-hhqs0rgDXhcc3cngEWzRFNkn8WfmuSRi3bzezzZczSaWsWIh8tRht8xA; msToken=maKuuFxdSIJXE6_3JTeh6Mdi-G4TI2g8YcSCbG7Tcy4oAkVni3PMCRZnbaf-gcMjmICfzfD7z0vZjFligRsTUNtc8IxrUo8WF2hVisBTd4rG6MB58O4=; tt_scid=Gcd6KFdZFQsToHyE-KZ1lKQ7OKjUszzHhdzmhsaYhyIONBR0hnhZ.hUVeJeuPG6w2037; IsDouyinActive=false',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
url = 'https://www.douyin.com/user/MS4wLjABAAAAjbYArk8QCfwPYui_lYqmcZV0CsFe4Hf4UJA5Vtaf5m_eSEiGTjQt8fEkathqBsct?modal_id=7280522597605870900&vid=7280881943699295522'
response = requests.get(url=url, headers=headers)
html_data = response.text
title = re.findall('video_title" content="(.*?)"/><meta', html_data)[0]
info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', html_data)[0]
html = requests.utils.unquote(info)
json_data = json.loads(html)
video_url = 'https:' + json_data['app']['videoDetail']['video']['bitRateList'][0]['playAddr'][0]['src']
print(title)
print(video_url)
