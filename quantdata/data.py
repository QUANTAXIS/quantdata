"""
数据模块

决定了数据的API,
mapping, dataclass, dataframe...  支持

"""
from typing import Text, Mapping

from pandas import DataFrame


class DataStructure:
    """ 通用数据结构 """

    def __init__(self, common):
        """ 可以是数据库中的数据, 也可以是http接口传回来的数据 """
        self.common = common

    def convert_to_platform(self, platform: Text):
        """ 转换到指定平台数据并返回新的实例 """
        return None

    def init_params(self, **params):
        """ 根据参数来处理数据 """

    def to_mapping(self) -> Mapping:
        """ 以字典的形式进行输出 """

    def to_df(self) -> DataFrame:
        """ 以dataframe形式输出 """

    def to_json(self) -> Text:
        """ 以json的形式进行输出 """

    def to_csv(self, filepath):
        """ 导出为csv文件 """
