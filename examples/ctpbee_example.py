try:
    from ctpbee import LooperApi, Vessel
    from time import sleep
except ImportError as e:
    raise ImportError("please install ctpbee")

from quantdata import QuantPlatform

platform = QuantPlatform(owner="tqsdk", support_platform="ctpbee", method="client")

print("info: waiting  API init")

while True:
    if platform.client.api:
        break
    sleep(5)

print("info: init successful ")

count = 0
while True:
    data = platform.fetch_data("SHFE.cu2001", level="tick", length=200).to_df()
    count += 1
    print(count)
    print(data)
    sleep(2)
