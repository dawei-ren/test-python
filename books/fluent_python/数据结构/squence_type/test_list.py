"""
列表推导式（list comprehension）(listcomps)
和
生成器表达式（generator expression）（genexps）
"""
import array


def string2unicode():
    """
    把一个字符串变成Unicode码位的列表
    一般形式
    """
    symbols = '$$$$$$$$'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)


def string2unicode_genexps():
    """
    把一个字符串变成Unicode码位的列表
    列表推导式
    通常的原则是，只用列表推导式来创建新的列表，并且尽量保持简短
    """
    symbols = '$$$$$$$$'
    codes = [ord(symbol) for symbol in symbols]
    print(codes)


"""
列表推导式可以帮助我们把一个序列或是其他可迭代类型中的元素过滤或者是加工，然后再新建一个列表。
python内置的filter和map函数组合起来也能达到这一效果，但是可读性打了不小的折扣。
"""


def string2unicode_filter_and_map():
    """
    把一个字符串变成Unicode码位的列表,并且过滤出>50的值
    使用filter和map来实现
    """
    # 采用列表推导式
    symbols = '!@#$%^&*()'

    beyond_ascii = [ord(s) for s in symbols if ord(s) > 50]
    print(beyond_ascii)

    # 采用filter和map, 很明显，列表推导式更容易读懂
    beyond_ascii_1 = list(filter(lambda c: c > 50, map(ord, symbols)))
    print(beyond_ascii_1)


"""
卡迪尔积：两个或者两个以上的列表中的元素对构成元组，这些元组构成的列表就是卡迪尔积。

卡迪尔积是一个列表，列表里的元素是由输入的可迭代类型的元素对构成的元组，因此，卡迪尔积列表的长度等于输入变量长度的乘积。

输入：
[1,2,3]   [a,b,c]
卡迪尔积列表：
[(1,a),(2,a),(3,a),(1,b),(2,b),(3,b),(1,c),(2,c),(3,c)]
"""


def get_t_shirts():
    """
    使用列表推导式计算卡迪尔积

    列表中是三种不同尺寸的T恤，每个尺寸都有两个颜色
    """
    colors = ["black", "white"]
    sizes = ["S", "M", "L"]
    t_shirts = [(size, color) for size in sizes for color in colors]
    print(t_shirts)


"""
生成器表达式
虽然也可以用列表推导式来初始化元组、数组或其他序列类型，但是生成器表达式是更好的选择。
因为生成器表达式背后遵循来迭代器协议，可以逐个产出元组，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里
生成器表达式明显更节省内存。

生成器表达式的语法跟列表推导式差不多，只不过把方括号换成圆括号而已。
"""


def genexps_tuple_array():
    """
    生成器表达式初始化元组和数组
    """
    symbols = '!@#$%^&*()'
    tuple_unicode = tuple(ord(symbol) for symbol in symbols)
    print(tuple_unicode)

    # array中的第一个参数指定来数组中的存储方式
    array_unicode = array.array("I", (ord(symbol) for symbol in symbols))
    print(array_unicode)


def list_and_list():
    """
    建立由列表组成的列表
    """
    board = [['-']*3 for i in range(3)]
    print(board)
    board[1][2] = 'x'
    print(board)

    # 相当于
    board1 = []
    for i in range(3):
        row = ['-']*3
        board1.append(row)

    # 注意：含有3个指向同一对象的引用列表是毫无用处的
    board2 = [['-']*3]*3
    print(board2)
    board2[1][2] = 'x'
    print(board2)
    # 可以看到三个都被改变了

    # 相当于
    row1 = ['-']*3
    board3 = []
    for i in range(3):
        board3.append(row1)


if __name__ == '__main__':
    # string2unicode()
    # string2unicode_genexps()
    # string2unicode_filter_and_map()
    # get_t_shirts()
    # genexps_tuple_array()
    list_and_list()