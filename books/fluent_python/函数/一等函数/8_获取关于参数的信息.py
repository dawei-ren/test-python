"""
获取关于函数参数的信息
"""
from inspect import signature


def clip(text, max_len=80):
    """
    在max_len前面或者后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


def test_code__():
    # 查看函数的默认参数
    print(clip.__defaults__)
    # 查看参数名称, 但是里面还包含有函数定义体中创建的局部变量
    print(clip.__code__.co_varnames)
    # 获取参数个数
    print(clip.__code__.co_argcount)
    # 所以函数的真正参数为
    print(clip.__code__.co_varnames[:clip.__code__.co_argcount])


def test_signature():
    """
    这样取参的方法太过麻烦，可以用inspect模块
    """
    sig = signature(clip)
    # print(str(sig))

    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    # inspect.signature对象有个bind方法，它可以把任意个参数绑定到签名中的型参上，所用的规则与实参的匹配形式一样。
    # 可以使用这个方法在真正调用函数前验证参数
    my_input_1 = {"text": "qwer mmmmmmmm"}
    sig.bind(**my_input_1)
    # 如果参数不符合规则会报错
    my_input_2 = {"text": "qwer mmmmmmmm", "a": "b"}
    # sig.bind(**my_input_2)


if __name__ == '__main__':
    # test_code__()
    test_signature()

