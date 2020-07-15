import xlwt

# 创建excel对象
wb = xlwt.Workbook(encoding='utf-8')
# 括号内参数为表名
ws = wb.add_sheet('whd')
# 参数1：行数
# 参数2：列数 从0开始计数
# 参数3：值   即单元格的内容
ws.write(0, 0, label='序号')
ws.write(0, 1, label='主机名')
ws.write(0, 2, label='是否启动')
ws.write(0, 3, label='15分钟内平均负载')
ws.write(0, 4, label='1分钟内平均负载')
ws.write(0, 5, label='5分钟内平均负载')
ws.write(0, 6, label='CPU利用率（本周平均）')
ws.write(0, 7, label='cpu总核数')
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
ws.write(0, 8, label='内存总数')
ws.write(0, 9, label='内存利用率（本周平均）')




ws.write(1, 0, label='1')
ws.write(1, 1, label='wode001')
ws.write(1, 2, label='未启动')
ws.write(1, 3, label='24%')

wb.save('D:/whd.xls')