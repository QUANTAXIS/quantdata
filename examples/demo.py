from quantdata import  QuantPlatform

platform = QuantPlatform(owner="tqsdk", support_platform="ctpbee", method="client")


from time import sleep
sleep(3)
while True:
    data = platform.fetch_data(local_symbol="SHFE.rb2001",level="tick", length=200).to_df()
    sleep(1)
    print(data.iloc[:-1].values[0])
