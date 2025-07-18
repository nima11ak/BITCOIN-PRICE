import requests
import matplotlib.pyplot as plt
from datetime import datetime


#دریافت قیمت بیتکوین در 30 روز گذشته

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily"

response = requests.get(url)

#اگر وضعیت پاسخ 200 باشه یعنی موفق بوده
if response.status_code == 200:
    data = response.json()



    #استخراج داده ها
    if "prices" in data:
        prices_data = data["prices"]

        #گرقتن زمان و تاریخ
        timestamps = [point[0] for point in prices_data]
        prices = [point[1] for point in prices_data]

        # تبدیل timestamp به تاریخ قابله فهم
        dates = [datetime.fromtimestamp(ts / 1000).strftime("%m-%d") for ts in timestamps]

        #رسم نمودار بیتکوین
        plt.figure(figsize=(10 , 5))
        plt.plot(dates, prices, label= " BITCOIN PRICE", color="orange")
        plt.xticks(rotation=45)
        plt.title("BITCOIN PRICE IN 30 DAYS")
        plt.xlabel("DATE")
        plt.ylabel("PRICE($)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    else:
        print("خطا اطلاعات قیمت دریافت نشد دوباره امتحان کنید یا اینترنت را چک کنید")

else:
    print(f" {response.status_code} :خطا در دریافت اطلاعات یا رسم نمودار ")

print(prices)

