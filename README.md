# Bastogne

高清电影下载站
---



所有数据采集自imax.im和互联网，仅供学习研究之用。

## 数据获取：

测试数据可用 `mongoimport` 从data目录 导入 MongoDB。
注意此为测试数据，本身并不完整，且存在部分错误
请参考 `tools/imax.py` 从 imax.im 抓取。


## 项目依赖：

* MongoDB
* tornado
* pymongo



## 已知问题

由于初次抓取时，只抓取了标题和下载地址等数据。其他数据是从豆瓣api匹配，所以部分影片存在匹配错误。
请直接参考`tools/imax.py` 从 imax.im 抓取完整数据。



