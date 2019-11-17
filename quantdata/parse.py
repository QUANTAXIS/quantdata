
from quantdata.helpers import get_seconds

class ParamsInterpreter:
    """ 
    参数解释器, 将外部统一调用的参数转换为目标函数可以理解的方式
    """
    def __init__(self, owner):
        self._owner = owner
    
    def parse(self, kwargs: dict):
        if self._owner == "tqsdk":
            print("tqsdk参数解析" )
            level = kwargs.get("level")
            local_symbol = kwargs.get("local_symbol")
            length = kwargs.get("length")
            if level != "tick":
                if not length:
                     return [local_symbol, get_seconds(level)], {}
                return [local_symbol, get_seconds(level), length], {}
        return [local_symbol, length], {}