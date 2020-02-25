import re

p = re.compile(r'word')  # 匹配第一次找到的结果
p1 = re.compile(r'\d\d\d')  # 匹配数字
p2 = re.compile(r'[2-9]')  # 范围匹配
p3 = re.compile(r'a{3}')  # 范围重复个数
p4 = re.compile(r'a{3,10}')  # 范围重复个数为3-10个
p5 = re.compile(r'[01]\d\d|2[0-4]\d|25[0-5]')  # 匹配001-255
# 匹配ip地址，(?:为非捕获组，就是findall不会捕获这个组
p6 = re.compile(r'(?:(?:[01]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d?\d|2[0-4]\d|25[0-5])')
p7 = re.compile(r'([1-9]\d{5}(18|19|20)\d{2}(0[1-9]|(10|11|12))[0-2][0-9]\d{3}[0-9Xx])|([1-9]\d{5}\d{2}(0[1-9]|(10|11|12))[0-2][0-9]\d{2}[0-9Xx])')


def search():
    """
    搜索第一个匹配项
    """
    string = 'hello aaaaaaword192.168.1.1'
    print(p.search(string))
    print(p1.search(string))
    print(p2.search(string))
    print(p3.search(string))
    print(p4.search(string))
    print(p5.search(string))
    print(p6.search(string))


def find_all():
    """
    搜索所有匹配项，并返回列表
    """
    string = 'hello aaaaaaword192.168.1.1qqq192.10.1.1word'

    res1 = p1.findall(string)
    print(res1)

    # 如果正则中有子组的化，只会返回子组中的内容
    p7 = re.compile(r'(\d\d)\d')
    res2 = p7.findall(string)
    print(res2)

    # 非捕获组，不让捕获正则表达式中本身的括号组，表达式中括号后面添加?:
    res3 = p6.findall(string)
    print(res3)


def find_iter():
    """
    将结果返回为迭代器，方便获取数据
    """
    string = 'hello aaaaaaword192.168.1.1qqq192.10.1.1word'
    res3 = p6.finditer(string)
    print(res3)
    for i in res3:
        print(i.group())
        print(i.span())


if __name__ == '__main__':
    # search()
    find_all()
    # find_iter()


