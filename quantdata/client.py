import re
from time import sleep
from tqsdk import TqApi
from threading import local, Thread

locale = local()

class LocalClient:

    def get(self):
        """
        取数据
        """

        raise NotImplementedError

    def set(self):
        """
            设置数据
        """  
        raise NotImplementedError


class TqsdkClient(LocalClient):

    def __init__(self, **kwargs):
        super().__init__()
        self.p = Thread(target=self.init_api, args=())
        self.p.start()
        self.api = None
        
    def init_api(self):
        
        self.api = TqApi()
        while True:
            sleep(60)


    def get(self, *argsm, **params):
        """ 调用他们的历史数据 """

        # tick数据
        if params.get("level") == "tick":
            return self.api.get_tick_serial(*self._parse_params(params))
        
        # 分钟线数据
        if params.get("level") != "tick":
            return self.api.get_kline_serial(*self._parse_params(params))

    def set(self):
        pass
    
    def _parse_params(self, params):
        """
        解析参数
        """
        level = params.get("level")
        local_symbol = params.get("local_symbol")
        length = params.get("length")
        if level != "tick":
            return [local_symbol, self.get_seconds(level), length]
        return [local_symbol, length]

    @staticmethod
    def get_seconds(level) -> int:
        """
        将level转换到秒
        * level: 数据等级
        """
        min_r = r"(\d{1,2})min"
        hour_r = r"(\d{1,2})h"
        day_r = r"(\d{1,2})day"
        if "min" in level:
            try:
                return int(re.match(min_r, level).group(1)) * 60
            except Exception:
                raise ValueError("你输入的level数据等级存在问题, 请检查是否符合1min这样的格式")
        if "h" in level:
            try:
                return int(re.match(hour_r, level).group(1)) * 3600
            except Exception:
                raise ValueError("你输入的level数据等级存在问题, 请检查是否符合1min这样的格式")
        if "day" in level:
            try:
                return int(re.match(day_r, level).group(1)) * 3600 * 24
            except Exception:
                raise ValueError("你输入的level数据等级存在问题, 请检查是否符合1day这样的格式")
