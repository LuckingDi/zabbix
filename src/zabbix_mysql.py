import pymysql
import time

db = pymysql.connect(host='123.196.116.236', user='root', passwd='Wode@0227', database='zabbix',
                     port=10001, charset='utf8')


# 获取主机id [(10084, 'wode069', 0), (10325, 'wode007', 0), (10326, 'wode174', 0), ...]
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


# 时间转换为时间戳
def type_time(data_time):
    # 转换为时间数组
    time_array = time.strptime(data_time, "%Y-%m-%d %H:%M:%S")
    # 转换为时间戳
    timestamp = int(time.mktime(time_array))
    return timestamp


# 获取监控值
def get_item_value(item_ids, time_from, time_till):
    t_from = type_time(time_from)
    t_till = type_time(time_till)
    item_values = []
    for item_id in item_ids:
        try:
            cursor = db.cursor()
            sql2 = 'select itemid,clock,value from history where {0}>clock and clock>{1} and itemid={2} '
            sql = sql2.format(t_till, t_from, item_id)
            cursor.execute(sql)
            results = cursor.fetchall()     # ((31303, 1594656703, 15.595506), (31303, 1594656763, 16.100756), ...)
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
    return item_values  # [(31044, 32.0), (31073, 2.9307576826388937)]


# 测试
if '__main__' == __name__:
    hosts = get_host_id()       # [(10084, 'wode069', 0), (10325, 'wode007', 0), (10326, 'wode174', 0), ...]
    print('************获取hosts************')
    print(hosts)
    print('*********************************')
    # hosts = [10329,10330]
    result = get_item_id(hosts)
    print('************获取result************')
    print(result)
    print('*********************************')
    item_ids = []
    for dicts in result:
        for i in dicts:
            item_ids.append(i[0])
    print('**************获取监控项id*****************')
    print(item_ids)
    print('******************************************')
    item_values = get_item_value(item_ids, '2020-07-14 00:00:00', '2020-07-15 00:00:00')    # [(31044, 32.0), (31073, 2.9307576826388937)]
    print('**************获取监控项id以及值*****************')
    print(item_values)  # [(29174, 0.626006944444444), (29170, 0.6233125000000006), (29175, 0.6236666666666679), (29161, 32.0), (29200, 1.8407107423611133)]
    print('******************************************')
    new_item = []       # [[10329,{'system.cpu.num': 32.0,'system.cpu.num': 32.0,...}],[10329,{'system.cpu.num': 32.0,'system.cpu.num': 32.0,...}]]
    for items in result:
        item2 = []
        for item in items:
            item2.append(item[1])
            item1 = {}  # {'system.cpu.num': 32.0,'system.cpu.num': 32.0}
            for item_va in item_values:
                if item[0] == item_va[0]:
                    item1[item[2]] = item_va[1]
                    item2.append(item1)    # [10329,{'system.cpu.num': 32.0,'system.cpu.num': 32.0}]
        new_item.append(item2)
    print('**********平凑主机id，和监控项以及value**************')
    print(new_item)
    print('******************************************')
    host_value = []
    for item in new_item:
        # for ii in item:     # [10329,{'system.cpu.num': 32.0,'system.cpu.num': 32.0}]
        for host in hosts:      # [(10084, 'wode069', 0), (10325, 'wode007', 0), (10326, 'wode174', 0), ...]
            if item[0] == host[0]:
                item.append(host[1])
                item.append(host[2])
        host_value.append(item)

    print(host_value)