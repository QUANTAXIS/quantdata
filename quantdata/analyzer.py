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
    "rice_quant": (RBarModel, RTickModel)
}


class Analyzer:
    """ 分析器 """
    pass
