from quantdata import  QuantPlatform

platform = QuantPlatform(owner="ctpbee", support_platform="tqsdk", method="client")

from time import sleep
sleep(3)
platform.fetch_data(local_symbol="rb2001",level="1min")
