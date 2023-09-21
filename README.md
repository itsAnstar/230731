# 仓库简介
#### 需要安装对应依赖，可选清华软件源或默认源站安装
- 「 国内源安装-清华大学 您可以运行以下命令」
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```
- 「 默认源站安装 您可以运行以下命令」
```
pip install -r requirements.txt
```
- auto-1 用来处理某音电商罗盘导出的素材视频表格源文件
- auto2&auto3 用来接受处理后的Excel文件并下载视频至指定的目录
- auto-3 仅下载模块、使用auto-3需要在DEMO第四列填充视频直链
## auto-1  (auto excel)-->normal
* 弹出资源管理器选择目标Excel文件 
* 对Excel文件进行处理
* DownloadInfo为退出并保存文件更改，并重命名文件，格式为：“video加当天日期月日”例如“video0801”
* VideoInfo为选择保留天数和保存文件名，保存退出文件

## auto-2 & auto3  (直链获取 & 请求下载)-->fixing
* 读取Excel
* 遍历视频链接所在第1列-->以视频URL为参数
* 获取第2列和第3列的值-->用以视频重命名
* 以requests.get方法获得response响应体
* 以re.findall方法匹配需要的json数据并传参
* 解析json-->正则匹配URL直链字段
* 以requests.get请求直链
* 下载直链文件
* 用HeadersDecoding程序来给Batch下载程序的cookie保活

## auto-3  (请求模块)-->normal
- 读取Excel
- 遍历视频直链所在第4列
- 请求直链下载文件-->rename && Save

