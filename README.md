
## auto-1  (auto excel)
* 读取excel-弹出资源管理器让用户自己选择文件 
* 按第4列扩展选定区域倒序 
* 删除第1、2、6、8、9、10、11、12、列 
* 判断表格第4列中每一行的内容是否为“0”，如果为0，删除这一行，如果不为“0”则不处理 
* 删除整个表格100行以后的内容，只保留前100行 
* 删除第四列
* 退出并保存文件更改，并重命名文件，格式为：“video加当天日期月日”例如“video0801”

## auto-2 & auto3  (直链获取 & 请求下载 & 异常规避)
* 读取Excel
* 遍历视频链接所在第1列-->以视频URL为参数
* 获取第2列和第3列的值-->用以视频重命名
* 以requests.get方法获得response响应体
* 以re.findall方法匹配需要的json数据并传参
* 解析json-->正则匹配URL直链字段
* 以requests.get请求直链
* 下载直链文件


## auto-3  --> 这部分功能已与auto2合并
* 下载重命名
* 整合文件夹 (待feat)