import pymysql
import time
import xlwt
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


db = pymysql.connect(host='127.0.0.1', user='root', passwd='', database='zabbix',
                     port=3306, charset='utf8')


# 获取主机id 
def get_host_id():
    hosts = []
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 创建sql 语句
        sql = "select hostid,host,status FROM hosts where host like 'wode%' or host like 'beihang%' or host like 'bit%'"
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for i in results:
            # 将停用的主机筛掉
            if i[2] == 0 and i[1] != 'wode124' and i[1] != 'wode174':
                hosts.append(i)
    except Exception:
        print('查询主机id失败')
    return hosts


# 获取监控项id
def get_item_id(hosts):
    item_key0 = "system.cpu.load[all,avg1]"
    item_key1 = "system.cpu.load[all,avg5]"
    item_key2 = "system.cpu.load[all,avg15]"
    item_key3 = "system.cpu.num"
    item_key4 = "system.cpu.util"
    item_key5 = "vm.memory.size[total]"
    item_key6 = "vm.memory.size[pavailable]"
    item_key7 = "vfs.dev.read.await[sda]"
    item_key8 = "vfs.dev.write.await[sda]"
    item_key9 = "vfs.dev.util[sda]"
    item_key10 = "vfs.dev.read.await[sdb]"
    item_key11 = "vfs.dev.write.await[sdb]"
    item_key12 = "vfs.dev.util[sdb]"
    item_key13 = "vfs.dev.read.await[sdc]"
    item_key14 = "vfs.dev.write.await[sdc]"
    item_key15 = "vfs.dev.util[sdc]"
    item_key16 = "vfs.dev.read.await[sdd]"
    item_key17 = "vfs.dev.write.await[sdd]"
    item_key18 = "vfs.dev.util[sdd]"

    all_item_id = []
    for i in hosts:
        try:
            cursor = db.cursor()
            sql2 = "select itemid,hostid,key_ from items where key_ in ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}')and itemid in (select itemid from items where hostid={19})"

            sql = sql2.format(item_key0, item_key1, item_key2, item_key3, item_key4, item_key5, item_key6, item_key7,
                              item_key8, item_key9, item_key10, item_key11, item_key12, item_key13, item_key14,
                              item_key15, item_key16, item_key17, item_key18, i[0])
            cursor.execute(sql)
            count = cursor.fetchall()
            all_item_id.append(count)
        except Exception:
            print("查询监控项id失败")

    return all_item_id


# 获取监控值
def get_item_value(item_ids, day):
    t_till = int(time.time())
    t_from = t_till - (86400*day)
    item_values = []
    for item_id in item_ids:
        try:
            cursor = db.cursor()
            sql2 = 'select itemid,clock,value from history where {0}>clock and clock>{1} and itemid={2} '
            sql = sql2.format(t_till, t_from, item_id)
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 0:
                sql3 = 'select itemid,clock,value from history_uint where {0}>clock and clock>{1} and itemid={2} '
                sql0 = sql3.format(t_till, t_from, item_id)
                cursor.execute(sql0)
                results = cursor.fetchall()
            sum_num = 0

            for value in results:
                sum_num += value[2]
            avg_value = float(sum_num/len(results))
            item_value = (item_id, avg_value,)
            item_values.append(item_value)
        except Exception:
            print(item_id+"获取监控值错误")
    db.close()
    return item_values


# 创建excel表格
def create_excel(host_values):
    # 创建excel对象
    wb = xlwt.Workbook(encoding='utf-8')
    # 括号内参数为表名
    ws = wb.add_sheet('whd')
    # 参数1：行数
    # 参数2：列数 从0开始计数
    # 参数3：值   即单元格的内容
    ws.write(0, 0, label='序号')
    ws.write(0, 1, label='主机名')
    ws.write(0, 2, label='是否启用')
    ws.write(0, 3, label='15分钟内平均负载')
    ws.write(0, 4, label='1分钟内平均负载')
    ws.write(0, 5, label='5分钟内平均负载')
    ws.write(0, 6, label='cpu总核数')
    ws.write(0, 7, label='内存利用率')
    ws.write(0, 8, label='内存总数')
    ws.write(0, 9, label='CPU利用率')
    ws.write(0, 10, label='sda磁盘读请求平均等待时间')
    ws.write(0, 11, label='sda磁盘写请求平均等待时间')
    ws.write(0, 12, label='sda利用率')
    ws.write(0, 13, label='sdb磁盘读请求平均等待时间')
    ws.write(0, 14, label='sdb磁盘写请求平均等待时间')
    ws.write(0, 15, label='sdb利用率')
    ws.write(0, 16, label='sdc磁盘读请求平均等待时间')
    ws.write(0, 17, label='sdc磁盘写请求平均等待时间')
    ws.write(0, 18, label='sdc利用率')
    ws.write(0, 19, label='sdd磁盘读请求平均等待时间')
    ws.write(0, 20, label='sdd磁盘写请求平均等待时间')
    ws.write(0, 21, label='sdd利用率')

    ws.write(1, 0, label=1)
    ws.write(1, 1, label=host_values[0][0])
    ws.write(1, 2, label=host_values[0][1])
    ws.write(1, 3, label=host_values[0][4])
    ws.write(1, 4, label=host_values[0][3])
    ws.write(1, 5, label=host_values[0][5])
    ws.write(1, 6, label=host_values[0][2])
    ws.write(1, 7, label=str(host_values[0][6])+'%')
    ws.write(1, 8, label=str(int(host_values[0][7] / 1073741824)) + 'G')
    ws.write(1, 9, label=str(host_values[0][8])+'%')
    ws.write(1, 10, label=host_values[0][9])
    ws.write(1, 11, label=host_values[0][10])
    ws.write(1, 12, label=host_values[0][11])
    i = 2
    for value in host_values[1:]:
        a = len(value)
        ws.write(i, 0, label=i)
        num = 1
        num2 = 0
        while num <= a:
            if num2 == 6:
                ws.write(i, num, label=str(value[num2]) + '%')
            elif num2 == 8:
                ws.write(i, num, label=str(value[num2]) + '%')
            elif num2 == 7:
                ws.write(i, num, label=str(int((value[num2] / 1073741824)+1)) + 'G')
            else:
                ws.write(i, num, label=value[num2])
            num += 1
            num2 += 1
        i += 1
    ti = time.strftime('%Y-%m-%d', time.localtime())
    excel_name = ti+'服务器使用情况日报.xls'
    wb.save('/root/log/'+excel_name)
    return excel_name,ti


# 发送邮件
def from_mail(excel_name):
    t_till = time.strftime('%Y-%m-%d', time.localtime())

    sender = ''     # 发送邮件账号
    receiver = ['', '']     # 接受邮件账号

    smtpserver = ''     # 服务器地址
    username = ''       # 发送邮件账号
    password = ''       # 账号密码
    mail_title = t_till + '日服务器报告'

    # 创建附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = Header(','.join(receiver))
    message['Subject'] = Header(mail_title, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('各位好:\r\r\t\t此封邮件为程序自动发出，目的是获取本周服务器的各项数据重要并发送给各位，以供各位了解这周服务器的使用情况，详情请查看附件!\r\r'
                            '\t\t附件中，第二项为主机名，第三项为是否启用（0为已启用），\r'
                            '\t\t第四项/第五项/第六项：为最近15、1、5分钟内机器运行进程队列中的平均进程数量，此值根据cpu核数而定，\r'
                            '\t\t不超过cpu总核数为有空闲（正常保持在cpu总核数的70%），如果此值等于CPU总核数为满载情况，如果超过CPU总核数则表示此机器负超过机器承受的范围，需要优化。\r'
                            '\t\t第7项为该机器CPU的总核数，第八项为此机器的内存利用率(百分比值)，第九项为机器的内存总量，第十项为机器的CPU利用率(百分比值)\n'
                            '\t\t后面几项都是机器上磁盘的读写速率，利用率等，作为参考数据，不作为重要数据（单位为：毫秒(ms)）。\r\r'
                            '\t\t请注意：附件中的值是我取本周所有时间点值的平均值，想要得知服务器使用详情，请登录：', ))
    # 构造附件
    att = MIMEApplication(open('/root/log/'+excel_name, 'rb').read())
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=excel_name)
    message.attach(att)

    smtpObj = smtplib.SMTP_SSL(host=smtpserver)
    smtpObj.connect(host=smtpserver, port=465)
    smtpObj.login(username, password)
    smtpObj.sendmail(sender, receiver, message.as_string())
    smtpObj.quit()
    retrun_message = "邮件发送成功"
    return retrun_message


# 测试
if '__main__' == __name__:
    hosts = get_host_id()
    result = get_item_id(hosts)
    item_ids = []
    for dicts in result:
        for i in dicts:
            item_ids.append(i[0])
    item_values = get_item_value(item_ids, day=1)    # [(31044, 32.0), (31073, 2.9307576826388937)]
    new_item = []
    for items in result:
        item2 = [items[0][1]]
        for item in items:
            for item_va in item_values:
                if item[0] == item_va[0]:
                    item2.append(item_va[1])    # [10329,{'system.cpu.num': 32.0,'system.cpu.num': 32.0}]
        new_item.append(item2)
    host_value = []
    for item in new_item:
        for host in hosts:
            if item[0] == host[0]:
                item[0] = host[2]
                item.insert(0, host[1])
        host_value.append(item)
    excel_name,ti = create_excel(host_value)
    return_message = from_mail(excel_name)

    print(ti+return_message)
