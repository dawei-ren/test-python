

def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """
    在max_len前面或者后面的第一个空格处截断文本

    添加注解，相比第8节中的函数，第一行添加注解，注解不会做任何处理，只是添加在函数的__annotations__属性中
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
