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


from quantdata.analyzer import Analyzer

class DataEntity:
    """ 
    通用数据实体
    提供大量的API
    """

    def __init__(self, common):
        """ 可以是数据库中的数据, 也可以是http接口传回来的数据 """
        self.common = common

    def to_mapping(self) -> Mapping:
        """ 以字典的形式进行输出 """

    def to_df(self) -> DataFrame:
        """ 以dataframe形式输出 """
        if isinstance(self.common, DataFrame):
            return self.common

    def to_json(self) -> Text:
        """ 以json的形式进行输出 """

    def to_csv(self, filepath):
        """ 导出为csv文件 """

    def resolve(self, **kwargs):
        """
        用户传来的处理参数， 还没想好怎么写
        """


class DataConvter(object):
    def __init__(self, owner, support_platform):
        """
        初始化数据转换转换器
        """
        self._owner = owner
        self._support_platform = support_platform

    def process_dataframe(self, origin_data: DataFrame, own_model, support_model):
        """ 
        处理结构体为DataFrame 
        根据桥梁重新命名参数
        * origin_data: 第一步从client请求过来的数据
        * own_
        """
        own_columns = origin_data.columns
        # 修改  
    
        attrs = {}
        refact ={}
        # 反转属性
        for i,v in support_model.__dict__.items():
            if not i.startswith("__"):
                attrs[v] = i
        for x in own_columns:
            try:
                refact[x] = getattr(own_model, x)
            except AttributeError as e:
                continue
        re_columns = {i:attrs[v] for i,v in refact.items()}

        origin_data = origin_data.rename(columns=re_columns)
        return origin_data

    def process_mapping(self, origin_data, own_model, support_model):
        """
        处理字典类型的属性
        """
        return []

    def process_json(self, origin_data, own_model, support_model):
        """
        处理json类型的数据
        """
        return ""

    def coverter(self, data, level, **kwargs) -> DataEntity:
        """ 
        开始进行转换 
        """
        print("data: ", data)

        own_model, des_model =  Analyzer.get_model(self._owner, level, self._support_platform)

        if isinstance(data, DataFrame):
            temp = self.process_dataframe(origin_data=data, own_model=own_model, support_model=des_model)

        if isinstance(data, dict):
            temp = self.process_mapping(origin_data=data, own_model=own_model, support_model=des_model)

        if isinstance(data, str):
            temp = self.process_json(origin_data=data, own_model=own_model, support_model=des_model)
        entity = DataEntity(temp)
        entity.resolve(**kwargs)
        return entity