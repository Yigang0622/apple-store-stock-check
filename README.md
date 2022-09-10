# Apple Store Stock Check

## 运行环境
Python3

## 依赖安装
```shell
pip3 install requests
```

## 运行
```shell
python3 main.py
```

## 配置抢不同型号
在main里面有示例了，每一次库存查询被抽象为一个线程类StockCheckThread，传入需要的SKU就行，可以自由发挥
```python
from check import *
from stock_check_thread import StockCheckThread
# 初始化查询线程，查询iphone 12
sku = AppleIphoneSKU.iPhone12128GGreen
t = StockCheckThread(sku=sku)
t.start()
# 查询 iPhone 13
sku2 = AppleIphoneSKU.iPhone13Pro256GBlue
t2 = StockCheckThread(sku=sku2)
t2.start()
```

## 添加SKU
在check.py的 class AppleIphoneSKU 中添加需要的SKU ，SKU 从 Apple Store 网页具体设备购买页面后选择完成配置后从链接中获得
如以下链接为购买 深空灰色，64 GB，无线局域网的iPad 2021，则他的SKU在链接末尾，为MK2K3CH/A
```shell
https://www.apple.com.cn/shop/buy-ipad/ipad-10-2/MK2K3CH/A
```
取的SKU后在类中添加上就好，或者初始化StockCheckThread线程时候直接传字段
```python3
class AppleIphoneSKU:
    iPhone13Pro256GBlue = 'MLTE3CH/A'
    ...
    ...
    ipad202164GBlackWifi2021 = 'MK2K3CH/A'
```


