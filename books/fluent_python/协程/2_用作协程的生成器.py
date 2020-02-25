"""
协程
"""


def simple_coro(a):
    """
    刚开始在yield中阻塞，然后send一个值，这个值会传给yield前面的变量，然后得到下一个yield后面的表达式计算的值，如果后面没有就是None
    """
    print('-> Started: a=', a)
    b = yield
    print('-> Received: b=', b)
    c = yield a + b
    print('-> Received: c =', c)


def main():
    my_coro = simple_coro(14)
    from inspect import getgeneratorstate
    # getgeneratorstate可以确定协程处于哪一个状态，目前是等待开始执行状态
    print(getgeneratorstate(my_coro))
    # 向前执行到协程到第一个yield表达式，然后产出a的值，并且暂停，等待为b赋值
    next(my_coro)
    # GEN_SUSPENDED 表示协程在yield处暂停
    print(getgeneratorstate(my_coro))
    # 把数字28发送给暂停的协程，计算yield表达式，得到28，然后把那个数字绑定给b，打印消息，产出a+b的值（42），然后协程暂停，等待为c赋值
    res = my_coro.send(28)
    # res为yield后面的表达式计算的值，也就吃产出的值
    print(res)
    my_coro.send(99)
    # print(getgeneratorstate(my_coro))


if __name__ == '__main__':
    main()