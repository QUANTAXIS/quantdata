from quantdata import  QuantPlatform

platform = QuantPlatform(owner="tqsdk", support_platform="ctpbee", method="client")

from time import sleep
sleep(3)
data = platform.fetch_data(local_symbol="SHFE.rb1910",level="tick", length=5000).to_df()

print(data)
