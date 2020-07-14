import pymysql

db = pymysql.connect(host='123.196.116.236', user='root', passwd='Wode@0227', database='zabbix',
                     port=10001, charset='utf8')


# 获取主机id [(10084, 'wode069', 0), (10325, 'wode007', 0), (10326, 'wode174', 0), ...}
def get_host_id():
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 创建sql 语句
        sql = "select hostid,host,status FROM hosts where host like 'wode%' or host like 'beihang%' or host like 'bit%'"
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        hosts = []
        for i in results:
            if i[2] == 0:
                hosts.append(i)
        return hosts
    except Exception:
        print('查询主机id失败')


# 获取监控项id
def get_item_id(hosts):
    item_key0 = 'net.if.in["enp4s0f0"]'
    item_key1 = 'net.if.out["enp4s0f0"]'
    item_key2 = 'net.if.in["enp4s0f1"]'
    item_key3 = 'net.if.out["enp4s0f0"]'
    item_key4 = "system.cpu.load[all,avg1]"
    item_key5 = "system.cpu.load[all,avg5]"
    item_key6 = "system.cpu.load[all,avg15]"
    item_key7 = "system.cpu.num"
    item_key8 = "system.cpu.util"
    item_key9 = "vfs.dev.read.await[sda]"
    item_key10 = "vfs.dev.write.await[sda]"
    item_key11 = "vfs.dev.util[sda]"
    item_key12 = "vfs.dev.read.await[sdb]"
    item_key13 = "vfs.dev.write.await[sdb]"
    item_key14 = "vfs.dev.util[sdb]"
    item_key15 = "vfs.dev.read.await[sdc]"
    item_key16 = "vfs.dev.write.await[sdc]"
    item_key17 = "vfs.dev.util[sdc]"
    item_key18 = "vfs.dev.read.await[sdd]"
    item_key19 = "vfs.dev.write.await[sdd]"
    item_key20 = "vfs.dev.util[sdd]"
    item_key21 = "vm.memory.size[total]"
    item_key22 = "vm.memory.size[pavailable]"
    #for i in hosts:
    try:
        cursor = db.cursor()
        print(11)
        sql2 = "select itemid,key_ from items where key_ in ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}'," \
               "'{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}')" \
               " and itemid in (select itemid  from items where hostid={23})"

        print(12)
        sql = sql2.format(item_key0, item_key1, item_key2, item_key3, item_key4, item_key5, item_key6, item_key7,
                          item_key8, item_key9, item_key10, item_key11, item_key12, item_key13, item_key14, item_key15,
                          item_key16, item_key17, item_key18, item_key19, item_key20, item_key21, item_key22, hosts)
        print(sql)
        cursor.execute(sql)
        count =cursor.fetchall()
        return count
    except Exception:
        print("查询监控项id失败")
    # 关闭数据库连接
    db.close()


# 测试
if '__main__' == __name__:
    # hosts = get_host_id()
    hosts = 10325
    result = get_item_id(hosts)
    print(result)