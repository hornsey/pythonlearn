#! /usr/bin/env python
# coding=utf-8
import sys
import time
import poplib
import smtplib


# 邮件发送函数
def send_mail():
    try:
        handle = smtplib.SMTP('smtp.163.com', 25)
        handle.login('ht@163.com', '123456')
        msg = 'To: 357776369@qq.com\r\nFrom:ht20042444@163.com\r\nSubject:hello\r\n'
        handle.sendmail('ht20042444@163.com', '357776369@qq.com', msg)
        handle.close()
        return 1
    except:
        return 0


# 邮件接收函数
def accpet_mail():
    try:
        p = poplib.POP3('pop.163.com')
        p.user('pythontab@163.com')
        p.pass_('420624')
        ret = p.stat()  # 返回一个元组:(邮件数,邮件尺寸)
        # p.retr('邮件号码')方法返回一个元组:(状态信息,邮件,邮件尺寸)
    except poplib.error_proto as e:
        print("Login failed:", e)
        sys.exit(1)

# 运行当前文件时，执行sendmail和accpet_mail函数
if __name__ == "__main__":
    send_mail()
    accpet_mail()
