# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# import time
#
#
# t_till = time.strftime('%Y-%m-%d', time.localtime())
#
# sender = 'it@wordemotion.com'
# receiver = ['wanghaodong@wordemotion.com', 'hahada@aliyun.com']
# # receiver = 'wanghaodong@wordemotion.com'
#
# smtpserver = 'smtp.exmail.qq.com'
# username = 'it@wordemotion.com'
# password = 'Azq123!@#'
# mail_title = t_till+'日服务器报告'
#
# # 创建附件的实例
# message = MIMEMultipart()
# message['From'] = sender
# message['To'] = Header(','.join(receiver))
# message['Subject'] = Header(mail_title, 'utf-8')
#
# # 邮件正文内容
# message.attach(MIMEText('各位好:\r\r\t\t此封邮件为程序自动发出，目的是获取本周服务器的各项数据重要并发送给各位，以供各位了解这周服务器的使用情况，详情请查看附件!\r\r'
#                         '\t\t附件中，第二项为主机名，第三项为是否启用（0为已启用），\r'
#                         '\t\t第四项/第五项/第六项：为最近15、1、5分钟内机器运行进程队列中的平均进程数量，此值根据cpu核数而定，\r'
#                         '\t\t不超过cpu总核数为有空闲（正常保持在cpu总核数的70%），如果此值等于CPU总核数为满载情况，如果超过CPU总核数则表示此机器负超过机器承受的范围，需要优化。\r'
#                         '\t\t第7项为该机器CPU的总核数，第八项为此机器的内存利用率(百分比值)，第九项为机器的内存总量，第十项为机器的CPU利用率(百分比值)\n'
#                         '\t\t后面几项都是机器上磁盘的读写速率，利用率等，作为参考数据，不作为重要数据（单位为：毫秒(ms)）。\r\r'
#                         '\t\t请注意：附件中的值是我取本周所有时间点值的平均值，想要得知服务器使用详情，请登录：server.wordemotion.com',))
# # 构造附件
# att = MIMEApplication(open('C:/Users/蓝色/Desktop/2020-07-12服务器.xls', 'rb').read())
# att["Content-Type"] = 'application/octet-stream'
# att.add_header('Content-Disposition', 'attachment', filename='2020-07-12服务器.xls')
# message.attach(att)
#
# smtpObj = smtplib.SMTP_SSL(host=smtpserver)
# smtpObj.connect(host=smtpserver, port=465)
# smtpObj.login(username, password)
# smtpObj.sendmail(sender, receiver, message.as_string())
# smtpObj.quit()
# print("邮件发送成功")