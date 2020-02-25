"""
迭代器模式


迭代器模式可以用来：
    访问一个聚合对象的内容而无需暴露
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
        return SentenceIterator(self.words)


class SentenceIterator:
    """
    迭代器
    """

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()

        self.index += 1
        return word

    def __iter__(self):
        return self
