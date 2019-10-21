# quantdata
nextgenereation data solution

> 击穿壁垒

## 快速使用

```
from quantdata import QuantPlatform

# 创建实例
platform = QuantPlatform(owner="ctpbee", support_platform="quantaxis", method="http", var="future")

# 初始化设置 
platform.initialize_http_config()

# 获取数据
data = platform.fetch_data(local_symbol="ap1910.SHFE", level="1min", df=True)

```

### 我们想实现什么
量化互联 ----->  让各个量化框架能够使用其他框架的数据 
                比如ctpbee的客户端使用强悍的qa数据，实现互联
      

## 期望
年底初步实现功能，大家都能快乐的按照一种标准来调用数据 

^_^

## 贡献代码 && 编写规范

提交PR，但请注意你的代码需要保持以下规范 
- 包名小写
- 类名大写开头, 驼峰命名  class XxxYxxx()
- 函数名 小写+下划线     def  xxx_xxx()
- 变量需要annotation
- 命名规则采用动宾结构
- 外部不可直接修改属性，需要通过set方法
- 属性访问通过property修饰
- 完整的函数注释, 同时参数需要通过 * age: 年龄  这样进行函数注解

## 当前支持平台 || 待支持平台 

当前已经支持平台
- None  

暂未支持平台
- quantaxis
- ctpbee
- vnpy
- rice_quant
- join_quant
- [tqsdk](https://github.com/shinnytech/tqsdk-python)  // 免费提供tick，k线数据哟

如果你有想支持的数据模型请添加issue或者 发送邮件联系沟通 
