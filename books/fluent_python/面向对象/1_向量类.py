from array import array
import math


class Vector2d:
    """
    向量类

    __slots__
        告诉解释器，这个类中的所有实例属性都在这了，这样，python会在各个实例中用类似元组的结构存储实例变量，
        从而避免使用消耗内存的__dict__属性

    __weakerf__:
        为了让对象支持弱引用，需要此属性，默认有此属性
        但是如果定义了__slots__，还要想把实例作为弱引用的目标，需要在__slots__中添加__weakerf__

    如果使用得当，__slots__可以显著节省内存，但是注意一下几点：
        每个子类都要定义__slots__属性，解释器会忽略继承的__slots__属性
        实例只能拥有__slots__中列出的属性，除非把__dict__加入其中，但是这样就失去了节省内存的功效
        如果不把__weakerf__加入其中，实例就不能作为弱引用的目标
    """
    # __slots__ = ('__x', '__y', '__weakerf__')
    type_code = 'd'

    def __init__(self, x, y):
        self.__x = float(x)  # 将属性标记为私有
        self.__y = float(y)

    @property   # 把读值方法标记为特性
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.type_code)]) + bytes(array(self.type_code, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def from_bytes(cls, octets):
        """
        从二进制中提取向量
        """
        # chr返回当前10进制或16进制对应的字符
        typecode = chr(octets[0])
        # memoryview() 函数返回给定参数的内存查看对象(Momory view)
        # 所谓内存查看对象，就是对象符合缓冲区协议的对象，为了给别的代码使用缓冲区里的数据，而不必拷贝，就可以直接使用。
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, format_spec=''):
        """
        如果format_spec 以p为后缀，那么在极坐标中显示向量，即<r, θ>，其中r是摸，θ是弧度，其他部分像往常一样
        :param format_spec:
        :return:
        """
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = abs(self), self.angle()
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        """
        求弧度
        """
        return math.atan2(self.y, self.x)

    def __hash__(self):
        """
        使向量可散列
        """
        return hash(self.x) ^ hash(self.y)


if __name__ == '__main__':
    v = Vector2d(1, 2)
    # print(bytes(v))
    # print(v.from_bytes(b'd\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@'))

    print(format(v, "0.3f"))
    print(format(v, "0.3fp"))
    # print(v.angle())