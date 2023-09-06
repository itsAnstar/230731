import requests
import time

url = "https://www.douyin.com/video/7271968816802860325"  # 将此处替换为您要访问的站点URL

# 创建一个Session对象
session = requests.Session()


def get_new_cookie():
    try:
        headers = {
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
