import pymysql

db = pymysql.connect(host='123.196.116.236', user='root', passwd='Wode@0227', database='zabbix', port=10001, charset='utf8')


try:
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 创建sql 语句
    sql = "select hostid,host,status FROM hosts where host like 'wode%' or host like 'beihang%' or host like 'bit%'"
    # 执行sql语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)
    hosts = []
    for i in results:
        if i[2] == 0:
            hosts.append(i)
    print(hosts)
except Exception:
    print('查询失败')
# 关闭数据库连接
db.close()