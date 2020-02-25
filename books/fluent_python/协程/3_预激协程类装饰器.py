"""
如果没有预激，那么协程没什么用
如果只是使用生成器定义一个协程，必须要调用next才能用，有了这个装饰器，就可以直接用了
"""

from functools import wraps


def coroutine(func):
    """
    预激协程装饰器
    """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


def averager():
    """
    普通协程
    计算平均值的协程
    :return:
    """
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


@coroutine
def averager_core():
    """
    预激协程
    计算平均值的协程
    :return:
    """
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


def test_averager():
    """
    测试普通协程
    """
    coro_avg = averager()
    # 普通协程必须要经过next
    next(coro_avg)
    print(coro_avg.send(10))
    print(coro_avg.send(20))


def test_averager_coro():
    """
    测试被预激装饰器装饰过的协程
    :return:
    """
    coro_avg = averager_core()
    print(coro_avg.send(10))
    print(coro_avg.send(20))


if __name__ == '__main__':
    # test_averager()
    test_averager_coro()




