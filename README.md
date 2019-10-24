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

### 流程与论证
这是一个兼容性数据框架，所以各家数据在内部实现应该是映射成一个Model,从数据层级上讲分为tick和bar数据。
那么如果实现我们想要的功能，请看以下流程，还请各位大佬指点 : 

1.收到数据指令，经过指令转换, 立即从数据源中取到数据。
2.拿到数据之后将数据拿到Analyzer<分析器>里面经过分析，拿到分析结果,
3.然后再将数据，以及分析结果拿到processor里面进行处理，拿到DataEntity<数据实体>, 返回给用户。
4.然后用户可以通过数据实体的接口拿到想要的数据


在这样的流程下面各家数据的兼容只需要实现一个映射即可！
> 具体的映射原理我是按照设计一个公有的结构，然后在各家映射里面添加公有数据映射。
 
如果你有什么好的意见 请邮件与我联系, 邮件地址: somewheve@gmail.com


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
