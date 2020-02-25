"""
    r.encoding                       #获取当前的编码
    r.encoding = 'utf-8'             #设置编码
    r.text                           #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
    r.content                        #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。

    r.headers                        #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None

    r.status_code                     #响应状态码
    r.raw                             #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()
    r.ok                              # 查看r.ok的布尔值便可以知道是否登陆成功
     #*特殊方法*#
    r.json()                         #Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
    r.raise_for_status()             #失败请求(非200响应)抛出异常
"""


import requests
import json


def requests_get():
    """
    不带参数的get请求
    :return:
    """
    r = requests.get('https://github.com/Ranxf')
    print(r.text)


def requests_get_params():
    """
    带参数的get请求
    :return:
    """
    params = {'wd': 'python'}
    r = requests.get(url='http://dict.baidu.com/s', params=params)
    print(r.text)


def requests_post_json():
    """
    post json请求
    :return:
    """

    headers = {
        "Upgrade-Insecure-Requests": "1",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
    }

    url = 'https://api.github.com/some/endpoint'
    data = {'some': 'data'}

    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    print(r.json())


def requests_post_json_header():
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}

    ret = requests.post(url, data=json.dumps(payload), headers=headers)

    print(ret.text)
    print(ret.cookies)


if __name__ == '__main__':
    # requests_post_json()
    requests_post_json_header()