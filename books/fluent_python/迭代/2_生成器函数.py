"""
生成器函数
    只要python函数的定义体中有yield关键字，该函数就是生成器函数，
    调用生成器函数时，会返回一个生成器对象，也就是说，生成器函数就是生成器工厂
    生成器就是迭代器


可以使用生成器函数代替1_迭代器模式中的SentenceIterator类
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    """
    可迭代对象

    此类可以迭代，是因为它实现类__iter__方法，构建并返回一个SentenceIterator(迭代器)实例
    """
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        # 这个return不是必要的，这个函数可以直接落空，自动返回
        # 不管有没有return语句，生成器函数都不会抛出StopIteration异常，而是在生成完全部值之后会直接退出
        return

