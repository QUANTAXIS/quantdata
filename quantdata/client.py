import re
from tqsdk import TqApi


class LocalClient:

    def get(self):
        raise NotImplemented


class TqSdkClient(LocalClient):

    def __init__(self, **kwargs):
        self.api = TqApi()

    def get(self, **params):
        """ 调用他们的历史数据 """
        if params.get("level") == "tick":
            return self.api.get_tick_serial(*self._parse_params(params))
        if params.get("level") != "tick":
            return self.api.get_kline_serial(*self._parse_params(params))

    def _parse_params(self, params):
        """
        将参数解析为tq可以理解的方式
        都需要返回一个*args
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
