"""
ctpbee数据模型
"""
from quantdata.model.base import TheBasicModel


class CTickModel(TheBasicModel):
    pass


class CBarModel(TheBasicModel):
    high_price: float = 0
    low_price: float = 0
    close_price: float = 0
    open_price: float = 0
    volume: int = 0
    local_symbol: int = None
