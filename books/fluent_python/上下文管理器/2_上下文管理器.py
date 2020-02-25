"""
上下文管理器对象存在的目的是管理with语句，就像迭代器的存在是为了管理for语句一样。

上下文管理器协议包括__enter__和__exit__两个方法。with语句开始运行时，会在上下文管理器对象上调用__enter__方法。
with语句运行结束后，会在上下文管理器用__exit__方法。


with open('a.txt') as f:
    src = f.read(60)

执行with后面的表达式得到的结果是上下文管理器对象，不过，把值绑定到目标变量上（as子句）是在上下文管理器上调用__enter__方法的结果
"""


class LookingGlass:
    """
    上下文管理器对象
    """
    # 除了self外，python调用此方法不会传入其他参数
    def __enter__(self):
        import sys
        # 把原来的sys.stdout.write方法保存在一个实例属性中，供后面使用
        self.original_write = sys.stdout.write
        # 为sys.stdout.write打猴子补丁，替换成自己编的方法
        sys.stdout.write = self.reverse_write
        # 返回字符串，这样才有内容存入目标变量
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        """
        这是用于取代sys.stdout.write的方法，把text的参数的内容反转，然后调用原来的实现
        """
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        如果一切正常，python调用exit方法时传入的参数是None、None、None；如果抛出了异常，这三个参数是异常数据
        :param exc_type: 异常类（例如ZeroDivisionError）
        :param exc_val: 异常实例。
        :param exc_tb:
        """
        import sys
        # 还原原来的sys.stdout.write方法
        sys.stdout.write = self.original_write
        # 如果有异常，而且是ZeroDivisionError类型，打印消息
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            # 告诉解释器，异常已经处理了
            return True


def test_with():
    """
    使用with调用上下文管理器类
    """
    # 上下文管理器是LookingGlass的实例，python在上下文管理器上调用__enter__方法，将返回结果绑定到lg上
    with LookingGlass() as lg:
        # 所有的print都走sys.stdout.write，已经被替换，所以打印出来都是反的
        print("abc")
        print(lg)

    # with调用结束后，python在上下文管理器上调用__exit__方法，这个方法又还原了原来的sys.stdout.write功能，所以可以正常打印
    print(lg)


def test_no_with():
    """
    不使用with，手动调用上下文管理器
    """
    lg = LookingGlass()
    print('abc')
    monster = lg.__enter__()
    print('abc')
    print(monster)
    lg.__exit__(None, None, None)
    print('abc')


if __name__ == '__main__':
    # test_with()
    test_no_with()
