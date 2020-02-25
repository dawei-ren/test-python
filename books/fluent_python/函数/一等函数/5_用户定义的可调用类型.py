"""
不仅python函数是真正的对象，任何python对象都可以表现的像函数，为此，只需要实现实例方法__call__
"""

import random


class BingoCage:
    """
    调用BingoCage实例，从打乱的列表中取出一个元素
    """
    def __init__(self, items):
        self._items = items
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    # 判断是否是可调用对象
    print(callable(BingoCage))

    # 测试加括号调用
    bingo = BingoCage([1, 2, 3])
    print(bingo.pick())
