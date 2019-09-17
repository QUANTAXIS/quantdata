"""
http client

需要兼容各家的数据获取
"""


class HttpClient:
    def __init__(self, support_platform, **kwargs):
        self.support_platform = support_platform
