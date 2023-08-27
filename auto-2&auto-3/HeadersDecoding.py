import requests
import time

url = "https://www.douyin.com/video/7218882382118571297"  # 将此处替换为您要访问的站点URL

# 创建一个Session对象
session = requests.Session()


def get_new_cookie():
    try:
        headers = {
            'Cookie': 'douyin.com; device_web_cpu_core=8; device_web_memory_size=8; webcast_local_quality=null; ttwid=1%7CMGhi6SefHMdUj-2dvOPmQ5zFKo7syPiQf_LdVo_sm9g%7C1691772890%7C900dcd00007c7a54c4bbe58a2c39823d8f1b21e41c12ab840b80faa23f39379b; passport_csrf_token=675830ff4a4ca21e4473ca5989477067; passport_csrf_token_default=675830ff4a4ca21e4473ca5989477067; s_v_web_id=verify_ll6twkdq_3GNpygbG_8yuj_4d9e_82E9_wsUAWUlhDd44; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; xgplayer_user_id=735486684335; __live_version__=%221.1.1.2573%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRVJSdFVNdzVjbkdaUXVWa0JaL2NiV2VwZjc4RDRsVjV1N0tCbnBiVTVtMVhUdUQ2WXVneEdrL1piaERTZkpqUCtkd1ZrV3pYZ0dtbHdwZWpxUkNlRkk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ==; csrf_session_id=dd1ddf27013aaa0a9322e17a826d917e; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1693515994580%2C%22type%22%3Anull%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; tt_scid=MPFPm-H3yLHGOeWDsP.4cO00GvmQVYBqS13MQr1HbPIlGgjqHghVEMGuHT8XS0Q26b5d; download_guide=%221%2F20230826%2F0%22; pwa2=%220%7C0%7C1%7C0%22; __ac_nonce=064ea671c003685871a61; __ac_signature=_02B4Z6wo00f01pgT0RwAAIDByGSV54lXnqaYM9WAAML6gfVahW6HaJ72IgaiEgGwaqSlvpH9PoJ1QOn7IxS9UFhytQJ-H4XibJmryNlNJy26e0f8w40Djv2cZlvtYxCfzEaJkubN7A-j5uEBf0; strategyABtestKey=%221693083422.32%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A3.65%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A250%7D%22; home_can_add_dy_2_desktop=%221%22; msToken=D2P2Pk-Kcz_XpPOZoicuRInMtpqAZ-LQRA0UJXT70q3ETCQz1R2ybfRgVrRwLZ58nSe1xw-WMmC9xGMrYAy6W7iQAWrMOBrUPGD_0w76nYfsBLTElmhw1b3kxJR2Gz0=; msToken=yxlyU_BAo6lKNOzJ_rkAgMcmUoHDiSLzfVkFP9d9u8LTpzF37ljMa9hP9w2P0zhHx_WmDVw7KDDbLqrpAOyJ1Px2SPs8BFCHd9FP2uRcYW9Tix3EbxmUB6HrX-UTGvk=; IsDouyinActive=false',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }

        # 清除会话中的Cookie
        session.cookies.clear()

        # 发送GET请求并保存当前Cookie
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            print("请求成功")
            return response.cookies.get_dict()  # 返回新的Cookie字典
        else:
            print(f"请求失败，状态码：{response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"请求发生异常：{e}")
        return None


# 构建初始Cookie
fixed_fields = 'douyin.com; device_web_cpu_core=8; device_web_memory_size=8; webcast_local_quality=null;'
initial_cookie = get_new_cookie()

if initial_cookie:
    print("初始Cookie:", initial_cookie)

# 循环，每隔10秒发送请求获取新的Cookie并打印
while True:
    new_cookie = f"‘cookie’: ‘{fixed_fields}{get_new_cookie()}’，"

    if new_cookie:
        print("新的Cookie:", new_cookie)

    time.sleep(10)  # 等待10秒
