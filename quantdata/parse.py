

class ParamsInterpreter:
    """ 
    参数解释器, 将外部统一调用的API能够
    """

    def __init__(self, support_platform):
        self._support_platform = support_platform
    
    def parse(self, kwargs: dict):
        if self._support_platform == "tqsdk":
            print("tqsdk参数解析" )
            


        return ([], {})