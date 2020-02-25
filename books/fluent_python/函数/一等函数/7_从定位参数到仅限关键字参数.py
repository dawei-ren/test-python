"""
python最好的特性之一就是提供了极为灵活的参数处理机制
"""


def tag(name, *content, cls=None, **attrs):
    """
    生成一个或多个HTML标签
    :param name: 传入单个定位参数， 生成一个指定名称的空标签
    :param content: 第一个参数后面的任意个参数都会被*content捕获，存入一个元组
    :param cls: cls参数只能作为关键字参数传入
    :param attrs: tag函数签名中没有明确指定名称的关键字参数会被**attrs捕获，存入一个字典
    :return:
    """
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))

    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)

    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    # 传入单个定位参数， 生成一个指定名称的空标签
    # print(tag("br"))
    # 第一个参数后面的任意个参数都会被*content捕获，存入一个元组
    # print(tag('p', 'hello'))
    # print(tag('p', 'hello', 'world'))
    # tag函数签名中没有明确指定名称的关键字参数会被**attrs捕获，存入一个字典
    # print(tag('p', 'hello', id=33))
    # cls参数只能作为关键字参数传入
    # print(tag('p', 'hello', 'world', cls='sidebar'))
    # 调用tag时，即便第一个定位参数也能作为关键字参数传入
    # print(tag(content='testing', name="img"))
    # 在my_tag前面加上**，字典中的所有元素作为单个参数传入，同名健会绑定到对应的具名参数上，余下的则被**attrs捕获
    my_tag = {'name': 'img', "title": "Sunset Boulevard", 'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))
