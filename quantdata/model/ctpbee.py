"""
ctpbee数据模型
"""
from quantdata.model.base import TheBasicModel, BarBaseModel, TickBaseModel


class CTickModel(TheBasicModel):
    high_price = TickBaseModel.high
    low_price = TickBaseModel.low
    close_price = TickBaseModel.close
    open_price = TickBaseModel.open
    volume = TickBaseModel.volume
    local_symbol = TickBaseModel.local_symbol
    datetime = TickBaseModel.datetime
    last_price = TickBaseModel.last

    open_interest = TickBaseModel.interest
    average_price = TickBaseModel.average

    limit_up = TickBaseModel.up_limit
    limit_down = TickBaseModel.down_limit
    
    ask_price_1 = TickBaseModel.ask_price_1
    ask_price_2 = TickBaseModel.ask_price_2
    ask_price_3 = TickBaseModel.ask_price_3
    ask_price_4 = TickBaseModel.ask_price_4
    ask_price_5 = TickBaseModel.ask_price_5
    
    ask_volume_1 = TickBaseModel.ask_volume_1
    ask_volume_2 = TickBaseModel.ask_volume_2
    ask_volume_3 = TickBaseModel.ask_volume_3
    ask_volume_4 = TickBaseModel.ask_volume_4
    ask_volume_5 = TickBaseModel.ask_volume_5

    bid_price_1 = TickBaseModel.bid_price_1
    bid_price_2 = TickBaseModel.bid_price_2
    bid_price_3 = TickBaseModel.bid_price_3
    bid_price_4 = TickBaseModel.bid_price_4
    bid_price_5 = TickBaseModel.bid_price_5
    
    bid_volume_1 = TickBaseModel.bid_volume_1
    bid_volume_2 = TickBaseModel.bid_volume_2
    bid_volume_3 = TickBaseModel.bid_volume_3
    bid_volume_4 = TickBaseModel.bid_volume_4
    bid_volume_5 = TickBaseModel.bid_volume_5



class CBarModel(TheBasicModel):
    high_price = BarBaseModel.high
    low_price = BarBaseModel.low
    close_price = BarBaseModel.close
    open_price = BarBaseModel.open
    volume = BarBaseModel.volume
    local_symbol = BarBaseModel.local_symbol
    datetime = BarBaseModel.datetime
