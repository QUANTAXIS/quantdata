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
