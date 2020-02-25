"""
yield from
    yield from x 表达式对x对象做的第一件事是，调用iter(x)，从中获取迭代器。因此x可以是任何可迭代对象。
    yield from 的主要功能是打开双通道，把最外层的调用方与最内层的子生成器连接起来，这样二者可以直接发送和产出值，还可以直接传入异常。

    之前发现，使用生成器的协程很麻烦，需要send，throw异常，close生成器，我们通过yield from 就可以避免这些大量处理异常的样板代码


yield from 使用：
    委派生成器
        包含yield from <iterable> 表达式的生成器
    子生成器
        从yield from 表达式中<iterable>部分获得的生成器
    调用方
        调用委派生成器的代码
"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    """
    子生成器

    计算平均值的协程
    :return:
    """
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield

        if term is None:
            break
        total += term
        count += 1
        average = total/count

    return Result(count, average)


def grouper(results, key):
    """
    委派生成器
    """
    while True:
        results[key] = yield from averager()


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    print(results)
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg': [40.9, 38.5, 44.3],
    'boys;kg': [39.0, 40.8, 43.2]
}


if __name__ == '__main__':
    main(data)
