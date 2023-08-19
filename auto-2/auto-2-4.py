import re
import json
import requests
import webbrowser
# 引入数据库依赖
from pymysql import *
# 入库字符转义
from pymysql.converters import escape_string

# 根据DY视频分享链接，获取视频链接
def getDouyinUrlByShareUrl(douyinShareUrl):
    # douyinShareUrl = 'https://v.douyin.com/jUAfreu/'
    # 请求头使用浏览器模拟的手机端请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 Edg/103.0.1264.62'
    }
    ree = requests.get(douyinShareUrl, headers=headers)
    # 对页面进行重定向处理 获取新的短视频链接
    new_url = ree.url
    # https://www.iesdouyin.com/share/video/7119013227169598754/?region=CN&mid=7119013266652285726&u_code=jdeie942&did=MS4wLjABAAAAaEl_MkpKRQQPoq06DAgPkUuQk8GsfUm8kn-He5q0h9FXhXqqi1RA5CE6_r0ngjn6&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&from=web_code_link
    # 7119013227169598754 即为视频 id
    # print(new_url)
    # 使用正则提取id
    id = re.search(r'/video/(.*?)/', new_url).group(1)
    # 提取带水印短视频链接地址
    # https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=7119013227169598754
    url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + id
    ree = requests.get(url, headers=headers)
    wm = ree.json()
    # 使用正则提取无水印视频链接
    result = wm['item_list'][0]['video']['play_addr']['url_list'][0].replace('wm', '')
    print("视频无水印url：" + result)
    return result

# 获取string中的链接
def get_url(content):
    if len(re.findall('[a-z]+://[\S]+', content, re.I | re.M)) > 0:
        return re.findall('[a-z]+://[\S]+', content, re.I | re.M)[0]
    return None

# 重定向url
def getRedirectUrl(url, header):
    # url:重定向的url
    response = requests.get(url, headers=header)
    return response.url

# 获取视频的详情
def getDouyinVideoInfo(douyinShareUrl):
    # douyinShareUrl = 'https://v.douyin.com/jUAfreu/'
    # dy官网
    douyinLink = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36'}
    if douyinLink.strip() is not None:
        if get_url(douyinShareUrl) is not None:
            # 分享链接需要重定向得到短视频真实链接
            # 通过分享链接重定向得到真实的url
            realUrl = getRedirectUrl(get_url(douyinShareUrl), headers)
            startUrl = realUrl[0:realUrl.index('?')]
            id = startUrl[startUrl.rindex('/') + 1:len(startUrl)]
            douyinParams = {'item_ids': id}
            if realUrl.__contains__('www.douyin.com/video'):
                douyinResponse = requests.get(url=douyinLink, params=douyinParams, headers=headers)
                # 抖音请求连接
                # requestsUrl = douyinResponse.url
                # print(requestsUrl)
                # 短视频详情body数据
                body = douyinResponse.text
                # print(body)
                # 短视频详情json数据
                data = json.loads(body)
                print("用户信息：" + data)
                try:
                    # 视频文案
                    videoTitle = data['item_list'][0]['desc']
                    # 视频带水印url
                    videoUrl = data['item_list'][0]['video']['play_addr']['url_list'][0]
                    # 视频无水印url
                    realVideoUrl = f'{videoUrl}'.replace('playwm', 'play')
                    print("视频文案：" + videoTitle)
                    print("视频带水印url：" + videoUrl)
                    print("视频无水印url：" + realVideoUrl)
                    # 在线打开无水印链接
                    # webbrowser.open(realVideoUrl)
                    return realVideoUrl
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    url = 'https://v.douyin.com/jUAfreu/'
    # 根据短视频分享链接，获取短视频链接
    print(getDouyinUrlByShareUrl("https://v.douyin.com/jUAfreu/"))
    print(" ======================================================= ")
    # 根据短视频分享链接，获取短视频详情
    print(getDouyinVideoInfo("https://v.douyin.com/jUAfreu/"))
    print(" ======================================================= ")