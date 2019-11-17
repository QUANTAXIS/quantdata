"""
简洁易用的装饰器 ，减少代码量
"""
import re

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
