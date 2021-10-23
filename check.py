import requests
import datetime


class AppleStoreCity:
    shanghai = '上海'


class AppleStoreLocation:
    # 上海环球港
    shanghaiGlobalHarbor = 'R683'
    # 环贸
    shanghaiIAPM = 'R401'
    # 南京东路
    shanghaiEastNanjingRoad = 'R359'
    # 浦东
    shanghaiPudong = 'R389'


class AppleIphoneSKU:
    # iPhone 13 pro 256G 远峰蓝
    iPhone13Pro256GBlue = 'MLTE3CH/A'
    iPhone12128GGreen = 'MGGY3CH/A'
    iPhone12256GGreen = 'MGH53CH/A'


class AppleStoreStockCheckResult:

    def __init__(self):
        self.store_name = ''
        self.available = False
        self.apple_product_sku = ''

    def __str__(self):
        return "Apple Store {} SKU {} \t 库存状态:{}".format(self.store_name, self.apple_product_sku, self.available)


def check_stock_availability(sku):
    print("check_stock_availability")
    print(datetime.datetime.now())
    results = []
    params = {
        'pl': True,
        'mt': 'compact',
        'parts.0': sku,
        'searchNearby': True,
        'store': AppleStoreLocation.shanghaiGlobalHarbor
    }
    url = 'https://www.apple.com.cn/shop/fulfillment-messages'

    try:
        result = requests.get(url, params=params).json()['body']['content']['pickupMessage']['stores']
        for each_store in result:
            store_name = each_store['storeName']
            city = each_store['city']
            availability = each_store['partsAvailability']
            if sku in availability:
                can_pickup = availability[sku]['storeSelectionEnabled']
                if city == AppleStoreCity.shanghai:
                    result = AppleStoreStockCheckResult()
                    result.store_name = store_name
                    result.available = can_pickup
                    result.apple_product_sku = sku
                    print(result)
                    results.append(result)
        return results
    except Exception as e:
        print(e)
        return []

