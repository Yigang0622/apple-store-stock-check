from check import *
import time
from stock_check_thread import StockCheckThread

freq = 3
print("Apple Store iPhone availability check started with frequency {}s".format(freq))

while True:
    sku = AppleIphoneSKU.iPhone12128GGreen
    t = StockCheckThread(sku=sku)
    t.start()
    time.sleep(freq)
    print()