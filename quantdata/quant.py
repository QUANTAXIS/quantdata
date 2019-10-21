"""
quantdata support
面向数据库和http接口的支持
"""


class QuantPlatform:
    """ 构建量化数据平台 """

    def __init__(self, owner, support_platform, method, var="future", **kwargs):
        """
            * owner: 当前你使用的平台
            * support_platform:  需要支持的平台数据
            * method: 连接属性 [http, tcp, mysql, mongo, sqlite]

            * var： 数据种类，默认为ctp期货数据，
        """
        self.owner = owner
        self.connection_link = ""
        self._support_platform = support_platform
        self._method = method
        self._var = var

    @property
    def method(self):
        return self._method

    @property
    def support_platform(self):
        return self._support_platform

    def initialize_database_config(self, info):
        """
        手动初始化数据库配置，创建数据库客户端
        * info: 数据库连接信息
        """

    def initialize_http_config(self, info):
        """
        初始化http接口信息
        * info：包含http的认证信息
        """

    def initialize_client_config(self, info):
        """
        针对客户端[ricequant, jq] 或者 tcp连接 等进行初始化
        * info: 包含基本的客户端认证信息
        """

    def measure_interface(self) -> bool:
        """
        测试接口是否正常进行工作
        返回True or False
        """
        if self.connection_link:
            return True
        return False

    def fetch_data(self, local_symbol, level, start=None, end=None, **kwargs):
        """
        此接口应该作为唯一取数据的通道
        获取数据，值得注意的是第一次取到的数据应该被载入成一个对象,
        然后通过kwargs中的参数进行处理,返回被处理过的数据

        * local_symbol: 本地合约代码名称
        * level: 数据级别 [tick, 1min-60min, 1h-nh, day, week,year]
        * start: 开始日期
        * end: 截至日期
        * kwargs: 数据处理
        """
