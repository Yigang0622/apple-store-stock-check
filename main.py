from check import *
from ifttt_util import *
import time

freq = 10
print("Apple Store iPhone availability check started with frequency {}s".format(freq))

while True:
    results = check_stock_availability(AppleIphoneSKU.iPhone13Pro256GBlue)
    results_filtered = [x for x in results if x.available]
    if len(results_filtered):
        send_ifttt_apple_stock_notification(results_filtered)
    time.sleep(freq)
    print()