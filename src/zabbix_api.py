from pyzabbix import ZabbixAPI

ZABBIX_SERVER = 'http://server.wordemotion.com/zabbix'

zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('wanghaodong@wordemotion.com', 'Wode@0227')
# 保存停运的主机
message = []


# 获取主机  [{'hostid': '10084', 'name': 'wode069'}, {'hostid': '10325', 'name': 'wode007'},]
def host_get():
    data = {
        "output": ["hostid", "name", "status"]
    }
    host_all_list = zapi.host.get(**data)
    host_list = []
    # 筛选出停用的主机
    for i in host_all_list:
        if i["status"] == '0':
            host_list.append(i)
        else:
            message.append(i["name"])
    return host_list


# 获取监控项 [{'itemid': '31040', 'hostid': '10325', 'key_': 'system.cpu.load[all,avg15]'}]
def items_get():
    data = {
        "output": ['itemid', 'hostid', 'key_'],
    }
    item_list = zapi.item.get(
        **data,
        search={
            "key_": "system.cpu.load[all,avg15]",
        }
    )
    its = []
    for i in item_list:
        if i['hostid'] == '10325':
            its.append(i)
    return its


# 获取监控信息值
def value_list():
    data = {
            "output": ["itemid","clock","value"],
        }
    v_list = zapi.history.get(
        itemids="31041",
        **data,
        history=0,
    )
    return v_list


if '__main__' == __name__:
    v_list = value_list()
    print(v_list)