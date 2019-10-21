"""
本模块存放者数据的模型,同时需要支持自定义的数据模型
同时你需要了解， 如果将基本模型转换到数据库模型 ? Powerful support

created at 2019-10-21
"""
# 排名不分先后 按照字母顺序
__support_platform__ = ['ctpbee', 'jq', 'quantaxis', 'rice_quant', 'vnpy']


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
