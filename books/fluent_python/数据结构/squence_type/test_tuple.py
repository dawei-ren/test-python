"""
元组：
不可变的列表
没有字段名的记录
"""
import os
from collections import namedtuple


def split_tuple():
    """
    元组拆包
    """
    # 普通拆包
    a, b, c = (1, 2, 3)
    print(a, b, c)

    # 使用*运算符把一个可迭代对象拆开作为函数的参数
    d = divmod(10, 8)
    print(d)
    t = (10, 8)
    d_1 = divmod(*t)
    print(d_1)

    # 不需要中间变量交换两个变量的值
    e, f = 1, 2
    print(e, f)
    f, e = e, f
    print(e, f)

    # _处理不需要的数据
    _, filename = os.path.split("/home/location/test.py")
    print(filename)

    # 使用*来处理剩下的元素
    g, h, *rest = range(5)
    print(g, h, rest)

    i, j, *rest1 = range(2)
    print(i, j, rest1)


def named_tuple():
    """
    具名元组
    collections.namedtuple是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类

    用namedtuple构建的类的实例所消耗的内存跟元组是一样的，因为字段名都被存在对应的类里面，
    这个实例跟普通的对象实例比起来也要小一些，因为python不会用__dict__来存放这些实例的属性
    """
    # 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。
    # 后者可以是有数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
    City = namedtuple('City', 'name country population coordinates')
    # 存放在对应字段里的数据要以一串参数的形式传入到构造函数中（注意，元组的构造函数却只接受单一的可迭代对象）
    tokyo = City('Tokyo', "JP", 36.933, (35.68, 139.69))
    print(tokyo)
    # 可以通过字段名称或者位置来获取一个字段的信息
    print(tokyo.population)
    # 可以跟元组一样迭代
    print('----------------')
    for i in tokyo:
        print(i)
    # _fields属性是一个包含这个类所有的字段名称的元组
    print(tokyo._fields)
    # _make 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟City(*delhi_data)是一样的
    t = ('Tokyo1', "JP1", 36.933, (35.68, 139.69))
    tokyo1 = City._make(t)
    # _asdict()把具名元组以collections.OrderDict的形式返回，我们可以利用它来把元组里的信息友好地呈现出来。
    print(tokyo1._asdict())


if __name__ == '__main__':
    # split_tuple()
    named_tuple()