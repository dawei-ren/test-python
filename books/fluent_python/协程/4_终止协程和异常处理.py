"""
协程中未处理的异常会向上冒泡，传给next函数或者send方法的调用方（即触发协程的对象）

generator.throw() ：
    致使生成器在暂停的yield表达式处抛出指定的异常。如果生成器处理类抛出的异常，代码会向前执行到下一个yield表达式，而产出的值会
    成为调用generator.throw方法得到的返回值，如果生成器没有处理抛出的异常，异常会向上冒泡。

generator.close()：
    关闭协程
"""

from functools import wraps
from inspect import getgeneratorstate


def coroutine(func):
    """
    预激协程类装饰器
    """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)

        next(gen)
        return gen

    return primer


@coroutine
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


def test_error_averager():
    """
    测试协程异常
    """
    coro_avg = averager()
    print(coro_avg.send(10))
    print(coro_avg.send(20))
    # 发送的值为字符串的话，导致协程内部有异常抛出
    print(coro_avg.send('10'))
    # 由于在协程内部没有处理异常，协程会终止，而且无法重新激活协程
    print(coro_avg.send(20))


class DemoException(Exception):
    """
    自定义异常类型
    """


def demo_exc_handling():
    print('-> coroutine started')
    # 使用try...finally 在协程结束的时候执行操作
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled Continuing')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')


def test_demo():
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.send(22)
    # 显示在yield表达式中暂停
    print(getgeneratorstate(exc_coro))
    # 传入自定义异常
    exc_coro.throw(DemoException)
    # 传入自定义异常不会导致协程终止, 但是如果不是自定义异常就会报错
    print(getgeneratorstate(exc_coro))
    # 关闭协程
    exc_coro.close()
    # 状态显示协程已关闭
    print(getgeneratorstate(exc_coro))


if __name__ == '__main__':
    # test_error_averager()
    test_demo()
