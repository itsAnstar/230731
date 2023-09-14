# 项目简介
#### 需要安装对应依赖，你可以安装清华源或自行安装
- 「 国内源安装-清华大学 您可以运行以下命令：」
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```
- 「 源站安装 您可以运行以下命令：」
```
pip install -r requirements.txt
```
- auto-1用来处理某音电商罗盘导出的素材视频表格源文件
- auto2&auto3用来接受处理后的Excel文件并下载视频至指定的目录
- 你也可以按照DEMO文件中的格式填充数据，直接启动getURLDownload-Batch-dev.py下载它平台上的其他视频

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
* 用HeadersDecoding程序来给Batch下载程序的cookie保活


