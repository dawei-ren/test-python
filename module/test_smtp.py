"""
使用smtp发送邮件

准备工作：
1. 首先需要在发送邮箱里面开启 POP3/SMTP服务 和 IMAP/SMTP服务, 设置-POP3/SMTP/IMAP中开启
2. 创建授权码，步骤1中会有提示
3. 代码中的密码一律使用授权码而不是邮箱密码
"""

from email.mime.text import MIMEText
import smtplib

"""
构造一个纯文本文件（MIMEText对象）
"""
# 第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证兼容性。
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

"""
发送邮件
"""
# 输入Email地址和口令:
from_addr = "ceshiyouxiang666@126.com"
# 配置授权码，注意不是密码
password = "shouquanma666"
# 输入SMTP服务器地址:
smtp_server = "smtp.126.com"
# 输入收件人地址:
to_addr = "ceshiyouxiang666@126.com"


server = smtplib.SMTP(smtp_server, 25)
# 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# login()方法用来登录SMTP服务器
server.login(from_addr, password)
# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



