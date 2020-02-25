"""
协议：
    协议是非正式的接口，在代码中不定义

python的序列协议：
    任何类，只需要标准的签名和语义实现类__len__和__getitem__这两个方法，就能用在任何期待序列的地方
"""


from array import array
import math
import reprlib
import numbers
import functools
import operator
import itertools


class Vector:
    """
    多维向量类
    """
    type_code = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        """
        将分量保存在一个数组中
        """
        self._components = array(self.type_code, components)

    def __iter__(self):
        """
        构建迭代器
        """
        return iter(self._components)

    def __repr__(self):
        """
        使用reprlib.repr()函数获取self._components的有限长度表示形式
        把字符串插入Vector的构造方法调用之前，去掉前面的array('d'和后面的)
        """
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.type_code)]) + bytes(self._components)

    def __eq__(self, other):
        """
        首先比个数，然后迭代两个对象中的元素，如果都相等，才相等
        """
        if len(self) != len(other):
            return False

        for a, b in zip(self, other):
            if a != b:
                return False
        return True

    def __hash__(self):
        # 创建一个生成器表达式，惰性计算各个分量的散列值，
        hashes = (hash(x) for x in self._components)
        # 使用规约函数reduce和xor函数计算聚合的散列值，第三个参数0是初始值
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        """
        取模求平方和在开根
        """
        return math.sqrt(sum(x * x for x in self))

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
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        """
        重写切片功能
        """
        # 获取实例所属的类
        cls = type(self)

        # 如果index的类型是slice对象(也就是[1:3]这种类型)，
        if isinstance(index, slice):
            # 调用类的构造方法，使用_components数组的切片构造一个新实例
            return cls(self._components[index])

        # 如果index是int或其他整数类型，那就返回相应的元素
        elif isinstance(index, numbers.Integral):
            return self._components[index]

        else:
            msg = '{cls.__name} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, item):
        cls = type(self)

        # 如果item只是一个字母，可能是shortcut_names中的一个
        if len(item) == 1:
            # 查找那个字母的位置
            pos = cls.shortcut_names.find(item)
            # 如果落在范围内，返回数组中对应的元素
            if 0 <= pos < len(self._components):
                return self._components[pos]
            msg = '{.__name__!r} object has no attribute {!r}'

            raise AttributeError(msg.format(cls, item))

    def __setattr__(self, key, value):
        """
        由于之前我们可以获取x、y等元素，但是这只是为了方便而临时取的，因此，不支持给这些属性赋值
        """
        cls = type(self)

        # 特别处理名称是单个字符的属性
        if len(key) == 1:
            # 如果属性在shortcut_names内或者是单个小写字母则返回相应的错误
            if key in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"

            else:
                error = ''

            if error:
                msg = error.format(cl_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        super().__setattr__(key, value)

    def angle(self, n):
        """
        计算某个角坐标
        """
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])

        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a

        else:
            return a

    def angles(self):
        """
        返回由所有角坐标构成的可迭代对象
        """
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, format_spec=''):
        if format_spec.endswith('h'):  # 超球面坐标
            format_spec = format_spec[:-1]
            # 使用itertools.chain函数生成生成器表达式，无缝迭代向量的模和各个角坐标
            coords = itertools.chain([abs(self)], self.angles())
            # 使用尖括号表示球面坐标
            outer_fmt = '<{}>'
        else:
            coords = self
            # 使用圆括号表示卡迪尔积坐标
            outer_fmt = '({})'

        # 创建生成器表达式，按需格式化各个坐标元素
        components = (format(c, format_spec) for c in coords)
        # 把以逗号分隔的格式化分量插入尖括号或圆括号
        return outer_fmt.format(', '.join(components))






if __name__ == '__main__':
    pass
