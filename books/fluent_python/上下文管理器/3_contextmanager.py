"""
contextmanager这个装饰器可以把简单的生成器函数变成上下文管理器，这样就不用创建类去实现管理器协议类
"""

import contextlib


@contextlib.contextmanager
def looking_glass():
    """
    在使用contextmanager装饰的生成器中，yield语句的作用是把函数的定义体分成两部分：
        yield语句前面的所有代码在with块开始时（解释器调用__enter__方法时）执行
        yield语句后面的代码在with块结束时（调用__exit__方法时）执行。
    """
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write

    msg = ''
    # 如果with块中抛出了异常，python解释器会捕获，然后在yield表达式里再次抛出，函数就会终止，永远无法到达yield后面的步骤，
    # 因此要捕获异常
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


def main():
    with looking_glass() as what:
        print('abc')
        print(what)

    print('abc')
    print(what)


if __name__ == '__main__':
    main()
