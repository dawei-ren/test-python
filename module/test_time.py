import time
import datetime
import pytz


def string2timestamp():
    """
    字符串时间转化为时间戳
    """
    a = "2013-10-10"
    time_array = time.strptime(a, "%Y-%m-%d")
    time_stamp = int(time.mktime(time_array))
    print(time_stamp)

    # 时间戳
    t = time.time()
    print(t, type(str(t)))


def timestamp2time():
    """
    时间计算
    """
    t1 = 1561098326687
    t2 = datetime.fromtimestamp(int(t1)/1000)
    print(t2)


def time_calc():
    """
    时间计算
    """
    t = datetime.fromtimestamp(int(1561098326687)/1000)
    now = datetime.now()
    print(t, now)
    res = now - t

    from_days = res.days
    from_hours = res.seconds//(60*60)
    from_seconds = res.seconds
    print(from_days, from_hours, from_seconds)


def timestamp2time():
    """
    时间戳转化为北京时间
    :return:
    """
    t1 = time.time()
    print(t1)

    tz = pytz.timezone('Asia/Shanghai')
    t = datetime.fromtimestamp(int(t1), tz).strftime('%Y-%m-%d %H:%M:%S')
    print(t)


if __name__ == '__main__':
    # string2timestamp()
    # timestamp2time()
    # time_calc()
    # timestamp2time()
    # t = time.time() + 30*24*3600
    d = datetime.datetime.now() + datetime.timedelta(days=30*3)
