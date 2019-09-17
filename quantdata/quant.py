"""
quantdata support
面向数据库和http接口的支持
"""


class QuantPlatform:
    """ 构建量化平台 """

    def __init__(self, owner, support_platform, **kwargs):
        """
            * owner: 当前你使用的平台
            * support_platform:  需要支持的平台数据

        """
        self.owner = owner
        self.support_platform = support_platform

    def initialize_database_config(self, info):
        """ 手动初始化数据库配置 """

    def initialize_http_config(self, info):
        """ 初始化http接口信息 """

    def measure_hickey(self) -> bool:
        """ 测试接口是否正常进行工作 """
        return True

    def catch_data(self, symbol, start, end, **kwargs):
        """ 获取数据 """

