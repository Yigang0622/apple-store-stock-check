import requests
from check import *

request_url = "https://maker.ifttt.com/trigger/miketech_new_comment/with/key/jV9PDLNh6RwvG4t0BxB2ENWE_p1uGd26jarTh-41223"


def send_ifttt_notification(msg):
    params = {
        'value1': 'App Store检测到库存',
        'value2': msg
    }
    res = requests.post(request_url, json=params)
    print(res.text)


def send_ifttt_apple_stock_notification(results):
    msg = ','.join([x.store_name for x in results])
    print(msg)
    send_ifttt_notification(msg)


# TEST
# result = AppleStoreStockCheckResult()
# result.store_name = "测试测试"
# send_ifttt_apple_stock_notification([result])
