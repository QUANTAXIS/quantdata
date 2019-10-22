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
    high = "high"


class BarBaseModel:
    local_symbol = "local_symbol"
    high = "high"
    low = "low"
    open = "open"
    close = "close"
    volume = "volume"
    datetime = "datetime"
    interest = "interest"
