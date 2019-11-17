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
            return self.api.get_tick_serial(*argsm, **params)
        
        # 分钟线数据
        if params.get("level") != "tick":
            return self.api.get_kline_serial(*argsm, **params)

    def set(self):
        pass
    

