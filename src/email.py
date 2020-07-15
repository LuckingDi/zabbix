import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # SMTP服务器
mail_user = "username"  # 用户名
mail_pass = "passwd"  # 密码(这里的密码不是登录邮箱密码，而是授权码)

sender = 'it@wordemotion.com'
receivers = ['wanghaodong@wordemotion.com', 'hahada@aliyun.com']

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')     # 发送者
message['To'] = Header("测试", 'utf-8')       # 接受者