"""
惰性实现

    前面的Sentence都不具备惰性，因为__init__方法迫切地构建好了文本中的单词列表，将其绑定在了self.words上，这样就要处理整个文本
列表使用的内存量可能和文本一样多。

re.finditer是re.findall的惰性版本，返回的不是列表，而是一个生成器
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    """
    可迭代对象的惰性实现
    """
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        """
        惰性实现生成器函数
        """
        for match in RE_WORD.finditer(self.text):
            yield match.group()
