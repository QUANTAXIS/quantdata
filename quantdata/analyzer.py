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
    def analyzer_data(self, own, level, data, destination):
        """
        将数据转换到从数据拥有着转换到目标场所
        先判读目标数据返回类型,然后转换到根据公有数据
        * own: 数据拥有者
        * level: 数据等级
        * data: 数据实体
        * destination: 需要转换到目标地
        """
        if own not in mapping:
            raise ValueError(f"你的数据厂商暂未支持, 我们仅仅支持: {str(list(mapping.keys()))}等数据厂商")

        bar_model, tick_model = mapping.get(own)
        # todo: 判断数据等级, 调用不同的模型进行处理
        
        # 返回分析结果
