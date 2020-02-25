"""
虽然列表既灵活又简单，但是，比如要存放1000万个浮点数的话，数组（array）的效率要高得多，
因为数组在背后存的并不是浮点对象，而是数字的机器翻译，也就是字节表述。这一点就跟C语言中的数组一样。
再比如，如果需要频繁对序列做先进先出的操作，deque（双端队列）的速度会更快。


数组：
如果我们需要一个只包含数字的列表，那么array.array比list更高效。
数组支持所有跟可变序列有关的操作，包括.pop、.insert和.extent。
另外，数组还提供从文件读取和存入文件的更快的方法，比如.frombytes和.tofile。
"""
from array import array
from random import random


def float_array():
    """
    创建一个有1000万个随机浮点数的数组
    把这个数组存放到文件里
    从文件里读取数组

    用array.fromfile从一个二进制文件里读取1000万个双精度浮点数只需要0.1秒，这比从文本文件里读取的速度快60倍
    因为后者会使用内置的float方法把每一行文字转化成浮点数。
    使用array.tofile写入到二进制文件，比以每一行一个浮点数的方式把所有的数字写入到文本文件要快7倍。
    另外，1000万个这样的数字在二进制文件里占用空间比文本文件少太多


    从python3.4开始，数组类型不再支持注入list.sort这种就地排序方法。要给数组排序的话，得用sorted函数新建一个数组

    a = array.array(a.typecode, sorted(a))
    """
    floats = array('d', (random() for i in range(10**7)))
    print(floats[-1])

    # 数组存入文件
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()

    # 创建数组用来读取文件
    floats2 = array('d')
    fp2 = open('floats.bin', 'rb')
    # 读取文件
    floats2.fromfile(fp2, 10**7)
    fp.close()
    print(floats2[-1])
    # 检查两个数组的内容是否一致
    print(floats2 == floats)


if __name__ == '__main__':
    float_array()
