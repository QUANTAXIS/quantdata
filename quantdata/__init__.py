"""
package explanation

* orm  存储各家数据关系的映射
* operation 处理底层的增删改查
* http 处理各个客户端的数据联动
* exception quantdata的异常机制

file explanation

# quantdata.py  核心文件入口
# helpers.py 辅助函数入口
# analyzer.py 负责转换数据到目标结构
# data.py 数据API

"""

__version__ = "0.1"
__author__ = "yutiansut && somewheve"

from quantdata.quant import QuantPlatform
