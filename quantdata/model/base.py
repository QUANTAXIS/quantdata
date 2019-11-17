"""
    存放了quantdata里面的基准模型

"""

from dataclasses import dataclass


@dataclass(init=False)
class TheBasicModel:
    """ 基本模型 """

    def __init__(self, **kwargs):
        pass

    def to_sql(self):
        """ 转换为数据库模型 """

    def to_fancy(self):
        """ 还没准备好咋写 """

    def parse_structure(self):
        """ 解析结构 """


class TickBaseModel:
    local_symbol = "local_symbol"
    exchange = "exchange"
    high = "high" # 最高
    low = "low" # 最低 
    open = "open" # 开盘
    close = "close" # 收盘价格 
    volume = "volume" # 成交量
    interest = "interest" # 持仓量
    last = "last" # 最新价格
    up_limit = "uplimit" # 涨停
    down_limit = "downlimit" # 跌停
    datetime = "datetime" # 时间戳
    average = "average" # 均价
    ask_price_1 = "ask_price_1" # 买一
    ask_price_2 = "ask_price_2" 
    ask_price_3 = "ask_price_3" 
    ask_price_4 = "ask_price_4" 
    ask_price_5 = "ask_price_5" 

    ask_volume_1 = "ask_volume_1" # 买一量
    ask_volume_2 = "ask_volume_2"
    ask_volume_3 = "ask_volume_3"
    ask_volume_4 = "ask_volume_4"
    ask_volume_5 = "ask_volume_5"

    bid_price_1 = "bid_price_1"  # 卖一价
    bid_price_2 = "bid_price_2"
    bid_price_3 = "bid_price_3"
    bid_price_4 = "bid_price_4"
    bid_price_5 = "bid_price_5"

    bid_volume_1 = "bid_volume_1" # 卖一量
    bid_volume_2 = "bid_volume_2"
    bid_volume_3 = "bid_volume_3"
    bid_volume_4 = "bid_volume_4"
    bid_volume_5 = "bid_volume_5"





class BarBaseModel:
    local_symbol = "local_symbol"
    high = "high"
    low = "low"
    open = "open"
    close = "close"
    volume = "volume"
    datetime = "datetime"
    interest = "interest"
