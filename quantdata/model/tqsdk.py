""" tqsdk的数据对接 """

from quantdata.model.base import TheBasicModel, TickBaseModel, BarBaseModel


class TTickModel(TheBasicModel):
    pass


class TBarModel(TheBasicModel):
    # *id: int, 1234(k线序列号)
    # *datetime: int, 1501080715000000000(K线起点时间(按北京时间)，自unix
    # epoch(1970 - 01 - 01
    # 00: 00:00
    # GMT)以来的纳秒数)
    # *open: float, 51450.0(K线起始时刻的最新价)
    # *high: float, 51450.0(K线时间范围内的最高价)
    # *low: float, 51450.0(K线时间范围内的最低价)
    # *close: float, 51450.0(K线结束时刻的最新价)
    # *volume: int, 11(K线时间范围内的成交量)
    # *open_oi: int, 27354(K线起始时刻的持仓量)
    # *close_oi: int, 27355(K线结束时刻的持仓量)

    high = BarBaseModel.high
    low = BarBaseModel.low
    close = BarBaseModel.close
    open = BarBaseModel.open
    volume = BarBaseModel.volume
    local_symbol = BarBaseModel.local_symbol
    datetime = BarBaseModel.datetime
    interest = BarBaseModel.interest
