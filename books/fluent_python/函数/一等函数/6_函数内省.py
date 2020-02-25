"""
除了__doc__，函数对象还有很多属性
"""


def factorial(n):
    """
    :return n!
    """
    return 1 if n < 2 else n*factorial(n-1)


# 查看函数属性
# print(dir(factorial))

# 查看函数专有而用户定义的对象没有的属性

print(sorted(set(dir(factorial))-set(dir(object))))
