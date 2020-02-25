"""
切片高级用法
"""


def main():
    s = "bicycle"

    # 以c为间隔切片
    print(s[::3])
    # 反向切片
    print(s[::-1])


def assignment():
    """
    给切片赋值
    :return:
    """
    l = list(range(10))
    print(l)
    l[2:5] = [20, 30]
    print(l)
    del l[5:7]
    print(l)


if __name__ == '__main__':
    # main()
    assignment()