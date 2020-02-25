"""
一等对象

一等对象定义：
    在运行时创建
    能赋值给变量或数据结构中的元素
    能作为参数传给函数
    能作为函数的返回结果
    在python中，整数、字符串和字典都是一等对象
    在python中，所有函数都是一等对象
"""


def factorial(n):
    """
    :return n!
    """
    return 1 if n < 2 else n*factorial(n-1)


print(factorial.__doc__)

"""
factorial.__doc__ 是函数对象众多属性中的一个，factorial是function类的实例
我们可以把factorial函数赋值给变量fact，然后通过变量名调用，我们还能把它作为参数传给map函数
"""

