"""
python的简单语法限制了匿名函数的定义体只能用纯表达式。
换句话说。lambda函数的定义体不能赋值，也不能使用while和try等python语句，

在参数列表中最适合使用匿名函数
"""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

# 使用lambda表达式反转拼写，然后依次给单词列表排序
res = sorted(fruits, key=lambda word: word[::-1])
print(res)