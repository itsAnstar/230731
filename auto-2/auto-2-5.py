
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 定义手机浏览器的User-Agent
user_agent = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
)

# 要测试的站点链接
site_url = "https://v.douyin.com/iJx76vB1/"  # 替换为实际的站点链接

# 发送模拟手机浏览器的请求
headers = {"User-Agent": user_agent}
response = requests.get(site_url, headers=headers)

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(response.content, "html.parser")

# 找到所有的缓存资源链接
cache_links = [link.get("href") for link in soup.find_all("link", rel="stylesheet")]

# 找到最大的数据包链接
max_cache_link = max(cache_links, key=lambda link: len(requests.get(link).content))

# 创建一个Excel工作簿并选择默认的活动工作表
wb = Workbook()
ws = wb.active

# 将链接写入Excel文件
ws.append(["Max Cache Link"])
ws.append([max_cache_link])

# 保存Excel文件
excel_filename = "max_cache_link.xlsx"
wb.save(excel_filename)
print(f"Max cache link written to {excel_filename}")
