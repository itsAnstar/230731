
## auto-1  (auto excel)
* 弹出资源管理器让用户自己选择文件 
* 对Excel文件进行处理
* 退出并保存文件更改，并重命名文件，格式为：“video加当天日期月日”例如“video0801”

## auto-2 & auto3  (直链获取 & 请求下载)
* 读取Excel
* 遍历视频链接所在第1列-->以视频URL为参数
* 获取第2列和第3列的值-->用以视频重命名
* 以requests.get方法获得response响应体
* 以re.findall方法匹配需要的json数据并传参
* 解析json-->正则匹配URL直链字段
* 以requests.get请求直链
* 下载直链文件


