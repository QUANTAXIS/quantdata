"""
数据处理器
"""


"""
数据模块

决定了数据的API,
mapping, dataclass, dataframe...  支持

"""
from typing import Text, Mapping

from pandas import DataFrame


class DataEntity:
    """ 通用数据实体 """

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


class DataConvter(object):

    def __init__(self, owner, support_platform):
        """
        初始化数据转换转换器
        """
        self._owner = owner
        self._support_platform = support_platform


    def coverter(self, data) -> DataEntity:
        """ 
        开始进行转换 
        """ 
        
        return 
