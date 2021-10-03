import threading
from check import *
from ifttt_util import *


class StockCheckThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        print("thread {} inited".format(self))

    def run(self) -> None:
        results = check_stock_availability(AppleIphoneSKU.iPhone12256GGreen)
        results_filtered = [x for x in results if x.available]
        if len(results_filtered):
            send_ifttt_apple_stock_notification(results_filtered)

    def __del__(self):
        print("thread {} del \n".format(self))