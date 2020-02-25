"""
bisect 模块包含两个主要函数，bisect和insort,两个函数都利用二分查找算法来在有序序列中查找或者插入元素
"""

import bisect
import random

HAYSTACK = [1, 4, 5, 6, 8]


def position():
    """
    通过bisect.bisect_right 来搜索needle在HAYSTACK中的位置，条件是在needle插入这个位置之后，HAYSTACK还能保持生序
    """
    needle1 = 2
    needle2 = 5

    position1 = bisect.bisect_right(HAYSTACK, needle1)
    position2 = bisect.bisect_right(HAYSTACK, needle2)
    print(position1, position2)


def insert():
    """
    排序很耗时，因此在得到一个有序序列之后，我们最好能狗保持它的有序
    insort(seq, item) 把变量item插入到序列seq中，并能保持seq的升序顺序
    """
    SIZE = 7

    random.seed(1729)

    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE*2)
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)


if __name__ == '__main__':
    insert()