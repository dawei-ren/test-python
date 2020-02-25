"""
内存视图

memoryview是一个内置类，它能让用户在不复制内容的情况下操作同一个数组里的不同切片

memoryview.cast的概念跟数组模块类似，能用不同的方式读写同一块内存数据，而且内容字节不会随意移动
"""
import array


def memory_view():
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    print(len(numbers))

    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0])


if __name__ == '__main__':
    memory_view()