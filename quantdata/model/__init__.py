"""
本模块存放者数据的模型,同时需要支持自定义的数据模型
同时你需要了解， 如果将基本模型转换到数据库模型 ? Powerful support

created at 2019-10-21
"""
# 支持平台, 排名不分先后
__support_platform__ = ['ctpbee', 'join_quant', 'quantaxis', 'rice_quant', 'vnpy', "tqsdk"]

from quantdata.model.ctpbee import CBarModel, CTickModel
from quantdata.model.join_quant import JBarModel, JTickModel
from quantdata.model.rice_quant import RBarModel, RTickModel
from quantdata.model.quantaxis import QBarModel, QTickModel
from quantdata.model.vnpy import VBarModel, VTickModel
from quantdata.model.tqsdk import TBarModel, TTickModel

__all__ = (
    CTickModel, CBarModel,
    JTickModel, JBarModel,
    RTickModel, RBarModel,
    QTickModel, QBarModel,
    VTickModel, VBarModel,
    TBarModel, TTickModel
)
