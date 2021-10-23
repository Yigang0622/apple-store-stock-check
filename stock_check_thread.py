import threading
from check import *
from ifttt_util import *
from playsound import playsound

class StockCheckThread(threading.Thread):

    def __init__(self, sku: AppleIphoneSKU):
        threading.Thread.__init__(self)
        self.sku = sku
        print("thread {} inited".format(self))

    def run(self) -> None:
        results = check_stock_availability(sku=self.sku)
        results_filtered = [x for x in results if x.available]
        if len(results_filtered):
            playsound("beep.wav")
            # send_ifttt_apple_stock_notification(results_filtered)


    def __del__(self):
        print("thread {} del \n".format(self))