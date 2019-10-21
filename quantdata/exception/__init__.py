"""
异常模块
一个优秀的框架是需要矫正用户的行为, 那么错误必须抛出
"""


class QuantDatabaseConnectionException(Exception):
    """ 连接数据库异常 """
    pass


class QueryException(Exception):
    """ 数据库查询异常 """
