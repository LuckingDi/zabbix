from pyzabbix import ZabbixAPI
import sys
import time

ZABBIX_SERVER = 'http://server.wordemotion.com/zabbix'

zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('wanghaodong@wordemotion.com', 'Wode@0227')


# 获取主机
# [{'hostid': '10084', 'name': 'wode069', 'status': '0'},
#   {'hostid': '10325', 'name': 'wode007', 'status': '0'},
#   {'hostid': '10326', 'name': 'wode174', 'status': '0'},]
def host_get():
    data = {
        "output": ["hostid", "name", "status"]
    }
    host_all_list = zapi.host.get(**data)
    return host_all_list


# 获取监控项 [{'itemid': '31040', 'hostid': '10325', 'key_': 'system.cpu.load[all,avg15]'}]
def items_get(host_all_list):
    keys = [
        'net.if.in["enp4s0f0"]',        # enp4s0f0接受数据
        'net.if.out["enp4s0f0"]',       # enp4s0f0发送数据
        'net.if.in["enp4s0f1"]',        # enp4s0f1接受数据
        'net.if.out["enp4s0f0"]',       # enp4s0f1发送数据
        "system.cpu.load[all,avg1]",    # 近1分钟CPU负载
        "system.cpu.load[all,avg5]",    # 近5分钟CPU负载
        "system.cpu.load[all,avg15]",   # 近15分钟CPU负载
        "system.cpu.num",               # cpu核数
        "system.cpu.util",              # CPU利用率
        "vfs.dev.read.await[sda]",      # sda磁盘读取请求avg等待时间(r_await)
        "vfs.dev.write.await[sda]",     # sda磁盘写入请求avg等待时间(r_await)
        "vfs.dev.util[sda]",            # sda利用率
        "vfs.dev.read.await[sdb]",      # sdb磁盘读取请求avg等待时间(r_await)
        "vfs.dev.write.await[sdb]",     # sdb磁盘写入请求avg等待时间(r_await)
        "vfs.dev.util[sdb]",            # sdb利用率
        "vfs.dev.read.await[sdc]",      # sdc磁盘读取请求avg等待时间(r_await)
        "vfs.dev.write.await[sdc]",     # sdc磁盘写入请求avg等待时间(r_await)
        "vfs.dev.util[sdc]",            # sdc利用率
        "vfs.dev.read.await[sdd]",      # sdd磁盘读取请求avg等待时间(r_await)
        "vfs.dev.write.await[sdd]",     # sdd磁盘写入请求avg等待时间(r_await)
        "vfs.dev.util[sdd]",            # sdd利用率
        "vm.memory.size[total]",        # 总内存
        "vm.memory.size[pavailable]",   # 内存使用率
    ]
    data = {
        "output": ['itemid', 'hostid', 'key_'],
    }
    item_list = []
    #for host in host_all_list:
    for key in keys:
        item_key_list = zapi.item.get(
                #**data,
                #hostids=host['hostid'],
            hostids='10325',
            search={
                "key_": key,
            }
        )
        if item_key_list:
            item_list.append(item_key_list)
        else:
            continue

    return item_list


# 时间转换为时间戳
def tyep_time(data_time):
    # 转换为时间数组
    timeArray = time.strptime(data_time, "%Y-%m-%d %H:%M:%S")
    # 转换为时间戳
    timestamp = int(time.mktime(timeArray))
    return timestamp


# 获取监控信息值
# [ {'itemid': '31041', 'clock': '1594310421', 'value': '0.89'},
#   {'itemid': '31041', 'clock': '1594310481','value': '0.89'}, ]
def value_list(item_id, t_from, t_till):
    data = {
            "output": ["itemid", "value"],
        }
    ti_from = tyep_time(t_from)
    ti_till = tyep_time(t_till)
    value_avg = []
    for itemid in item_id:
        v_list = zapi.history.get(
            itemids=itemid,
            **data,
            history=0,
            time_from=ti_from,
            time_till=ti_till,
        )
        sum = 0
        sum1 = 0
        for i in v_list:
            sum = sum + float(i['value'])
            sum1 = sum1 + 1
        avg = sum / sum1
        value_avg.append({'itemid':itemid, 'avg': avg})
    return value_avg


if '__main__' == __name__:
    hosts = host_get()      #[{'hostid': '10084', 'name': 'wode069', 'status': '0'},{'hostid': '10325', 'name': 'wode007', 'status': '0'},
    ites = items_get(hosts) #
    item_id=[]
    for i in ites:
        for e in i:
            item_id.append(e['itemid'])

    avg_num = value_list(item_id, '2020-07-09 14:00:00', '2020-07-09 16:00:00')

    print(avg_num)
