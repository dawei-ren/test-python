import os


def test_remove_file():
    my_file = 'text.txt'

    if os.path.exists(my_file):
        # 删除文件，可使用以下两种方法。
        os.remove(my_file)
    else:
        print('no such file:%s' % my_file)
