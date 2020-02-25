from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    """
    让协程返回值

    普通协程
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


def test1():
    """
    这样使用不会产出值，因为当发送None的时候会终止循环，导致协程结束，会抛出StopIteration错误
    :return:
    """
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(20)
    coro_avg.send(None)


def test2():
    """
    如果调用方捕捉StopIteration错误，就可以得到协程的返回值
    :return:
    """
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(20)
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        result = exc.value

    print(result)


"""
yield from

    yield from结构会自动捕获StopIteration异常
    
    把value属性的值变成yield from的值
    
    在生成器gen中使用yield from subgen()时，subgen会获得控制权，把产出的值传给gen的调用方，即调用方可以直接控制subgen，
    于此同时，gen会阻塞，等待subgen终止。
    
    yield from 可用于简化for循环中的yield表达式
"""


def gen1():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i


def gen2():
    """
    简化gen1中的for循环中的yield表达式
    """
    yield from 'AB'
    yield from range(1, 3)


def test3():
    print(list(gen1()))
    print(list(gen2()))


if __name__ == '__main__':
    # test1()
    # test2()
    test3()