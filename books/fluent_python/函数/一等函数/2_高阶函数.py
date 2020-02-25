"""
接受函数作为参数，或者把函数作为结果返回的函数是高阶函数

高阶函数有 map、filter、reduce、apply和sorted

map、filter 可以被列表推倒式或生成器表达式替换
"""
import math
from functools import reduce


def test_high_level_fun():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    # sorted函数 任何参数函数都能作为key参数的值
    sorted_fruits = sorted(fruits, key=len)
    print(sorted_fruits)

    # map函数，对序列挨个处理，将处理完的序列返回
    res1 = list(map(math.factorial, range(6)))
    print(res1)
    res2 = [math.factorial(n) for n in range(6)]
    print(res2)

    # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
    # 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中
    res3 = list(map(math.factorial, filter(lambda n: n % 2, range(6))))
    print(res3)
    res4 = [math.factorial(n) for n in range(6) if n % 2]
    print(res4)

    # reduce函数会对参数序列中元素进行累积。
    def add(x, y):
        return x + y

    res5 = reduce(add, [1, 2, 3, 4, 5])
    print(res5)


if __name__ == '__main__':
    test_high_level_fun()
