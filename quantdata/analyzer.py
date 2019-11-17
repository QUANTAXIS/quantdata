"""
数据分析器 -----> hope it will relax you

主要集中在数据分析，然后进行转换
"""
from quantdata.model import *

# 维护的一个关系
mapping = {
    "vnpy": (VBarModel, VTickModel),
    "quantaxis": (QBarModel, QTickModel),
    "ctpbee": (CBarModel, CTickModel),
    "join_quant": (JBarModel, JTickModel),
    "rice_quant": (RBarModel, RTickModel),
    "tqsdk": (TBarModel, TTickModel)
}


class AnalyzeResult:
    """ 经过分析得到的结果 """


class Analyzer:
    """ 分析器 """

    @classmethod
    def get_model(self, own, level, destination):
        """
        返回用有的model和即将转换的Model
        * own: 数据拥有者
        * level: 数据等级
        * destination: 需要转换到目标地
        """
        if own not in mapping or destination not in mapping:
            raise ValueError(f"你的数据厂商暂未支持, 我们仅仅支持: {str(list(mapping.keys()))}等数据厂商")

        own_bar_model, own_tick_model = mapping.get(own)
        # todo: 判断数据等级, 调用不同的模型进行处理
        des_bar_model, des_tick_model = mapping.get(destination)

        if level != "tick":
            return own_bar_model, des_bar_model

        else:
            return own_tick_model, des_tick_model
            

        


        
        
