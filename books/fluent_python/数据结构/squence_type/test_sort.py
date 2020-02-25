"""
探讨两种排序方法
"""


def main():
    """
    有两种排序方法，一种是list.sort：会就地排序列表，不会产生新的列表，不会把列表复制一份
    sorted函数：它会新建一个列表作为返回值，这个方法可以接受任何形式的可迭代对象，甚至包括不可变序列或生成器

    它们都有reverse参数，如果设定为True，会降序排列
    它们都有key参数：一个只有一个参数的函数，这个函数会作用在序列里的每一个元素上，所产生的结果将是排序算法依赖的对比关键字
    :return:
    """
    fruits = ['grape', 'apple', 'banana']

    a = sorted(fruits)
    print(fruits)  # 原列表没有发生任何变化
    print(a)

    print(sorted(fruits, reverse=True))
    print(sorted(fruits, key=len))

    fruits.sort()
    print(print(fruits))  # 原列表发生了变化


if __name__ == '__main__':
    main()