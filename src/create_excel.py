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
ws.write(0, 3, label='CPU利用率（本周平均）')

ws.write(1, 0, label='1')
ws.write(1, 1, label='wode001')
ws.write(1, 2, label='未启动')
ws.write(1, 3, label='24%')

wb.save('D:/whd.xls')