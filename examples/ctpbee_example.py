from cmath import isnan

from ctpbee import Vessel, LooperApi
from ctpbee.constant import Direction
from ctpbee.indicator import Indicator
from pandas import DataFrame
from tqsdk.tafunc import time_to_datetime

try:
    from time import sleep
except ImportError as e:
    raise ImportError("please install ctpbee")

from quantdata import QuantPlatform

platform = QuantPlatform(owner="tqsdk", support_platform="ctpbee", method="client")

print("info: waiting  API ininant")

while True:
    if platform.client.api:
        break
    sleep(1)

print("info: init successful ")

count = 0
while True:
    data = platform.fetch_data("SHFE.cu2001", level="15min", length=1000).to_df()
    import numpy as np

    if not np.isnan(data['high_price'][999]):
        break
    print(data)
    sleep(1)


class DoubleMaStrategy(LooperApi):
    allow_max_price = 5000  # 设置价格上限 当价格达到这个就卖出 防止突然跌 止盈
    allow_low_price = 2000  # 设置价格下限 当价格低出这里就卖 防止巨亏 止损

    def __init__(self, name):
        super().__init__(name)
        self.count = 1
        self.api = Indicator()
        # self.api.open_json("zn1912.SHFE.json")
        self.pos = 0
        self.instrument_set = ['cu2001.SHFE']

    def on_bar(self, bar):
        # todo: 均线 和 MACD 和 BOLL 结合使用
        """ """
        am = self.api
        am.add_bar(bar)
        if not am.inited:
            return
        # 收盘
        close = am.close
        # 压力 平均 支撑
        # top, middle, bottom = am.boll()
        # DIF DEA DIF-DEA
        macd, signal, histo = am.macd()

        if self.allow_max_price <= close[-1] and self.pos > 0:
            self.action.sell(bar.close_price, self.pos, bar)

        if self.allow_low_price >= close[-1] and self.pos > 0:
            self.action.sell(bar.close_price, self.pos, bar)
        # 金叉做多 和 均线>平均
        if histo[-1] > 0:
            if self.pos == 0:
                self.action.buy(bar.close_price, 1, bar)

            elif self.pos < 0:
                self.action.cover(bar.close_price, 1, bar)
                self.action.buy(bar.close_price, 1, bar)
        # 死叉做空
        elif histo[-1] < 0:
            if self.pos == 0:
                pass
            elif self.pos > 0:
                self.action.sell(bar.close_price, 1, bar)
                self.action.short(bar.close_price, 1, bar)

    def on_trade(self, trade):
        if trade.direction == Direction.LONG:
            self.pos += trade.volume
        else:
            self.pos -= trade.volume

    def init_params(self, data):
        """"""
        # print("我在设置策略参数")
        #


double_ma = DoubleMaStrategy("double_ma")


def run_main(result):
    vessel = Vessel()
    result = list(result.values())
    for x in result:
        x['datetime'] = x['datetime'].to_pydatetime()
    print(len(result))
    vessel.add_data(result)
    vessel.add_strategy(double_ma)
    vessel.set_params({"looper":
                           {"initial_capital": 2000000,
                            "commission": 0.005,
                            "deal_pattern": "price",
                            "size_map": {"cu2001.SHFE": 15},
                            "today_commission": 0.005,
                            "yesterday_commission": 0.02,
                            "close_commission": 0.005,
                            "slippage_sell": 0,
                            "slippage_cover": 0,
                            "slippage_buy": 0,
                            "slippage_short": 0,
                            "close_pattern": "yesterday",
                            },
                       "strategy": {}
                       })
    vessel.run()
    from pprint import pprint
    result = vessel.get_result()
    pprint(result)


def process_data(data: DataFrame):
    data['datetime'] = data['datetime'].apply(lambda time: time_to_datetime(time))
    data['local_symbol'] = data['symbol'].apply(lambda symbol: ".".join(reversed(symbol.split("."))))
    data['type'] = "bar"
    return data.to_dict("index")


if __name__ == '__main__':
    result = process_data(data)
    run_main(result)
