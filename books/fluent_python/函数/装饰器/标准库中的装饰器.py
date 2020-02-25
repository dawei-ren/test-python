"""
装饰器

python内置了三个用于装饰方法的函数：property，classmethod 和 staticmethod

还有几种更加厉害的装饰器
"""


import time
import functools


def clock(func):
    """
    普通装饰器
    """
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__

        args_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, args_str, result))
        return result

    return clocked


def clock_wraps(func):
    """
    functools.wraps
    协助构建行为良好的装饰器，普通装饰器不支持关键字参数，而且遮盖了被装饰函数的__name__和__doc__属性，使用functools.wraps装饰器能
    把相关的属性从func复制到clocked中。此外，这个版本还能正确处理关键字参数
    """

    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0

        name = func.__name__

        args_lst = []
        if args:
            args_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ["%s=%r" % (k, w) for k, w in sorted(kwargs.items())]
            args_lst.append(', '.join(pairs))

        args_str = ', '.join(args_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, args_str, result))
        return result

    return clocked


@functools.lru_cache(maxsize=128, typed=False)
@clock_wraps
def fibonacci(n):
    """
    斐波那契数列第n个值

    clock_wraps: 前面实现的计时装饰器

    functools.lru_cache：是非常使用的装饰器，它实现了备忘功能，这是一项优化技术，它把耗时的函数的结果保存起来，避免传入相同的参数
    时重复计算，一段时间不用的缓存条目会被扔掉，可以极大的优化递归算法
    1：maxsize参数指定存储多少个调用的结果。缓存满了之后，旧的结果会被扔掉，maxsize应该设为2的幂
    2：typed参数如果设为True，把不同参数类型得到的结果分开保存，即把通常认为相等的浮点数和整数参数区分开
    3：被lru_cache装饰的参数都必须是可散列的
    """
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(30))

