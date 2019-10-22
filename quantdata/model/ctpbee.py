"""
ctpbee数据模型
"""
from quantdata.model.base import TheBasicModel, BarBaseModel, TickBaseModel


class CTickModel(TheBasicModel):
    pass


class CBarModel(TheBasicModel):
    high_price = BarBaseModel.high
    low_price = BarBaseModel.low
    close_price = BarBaseModel.close
    open_price = BarBaseModel.open
    volume = BarBaseModel.volume
    local_symbol = BarBaseModel.local_symbol
    datetime = BarBaseModel.datetime
