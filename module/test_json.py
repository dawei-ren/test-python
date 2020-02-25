"""
python json模块骚操作
"""
import json


def main():
    dic = {"nihao":1, "你好":2}
    js = json.dumps(dic)
    print(js)

    # 骚操作之显示显示汉语
    js2 = json.dumps(dic, ensure_ascii=False)
    print(js2)

    # 骚操作之格式化显示
    js3 = json.dumps(dic, ensure_ascii=False, indent=4)
    print(js3)


if __name__ == '__main__':
    main()
