result = [
	(
		(29174, 10084, 'system.cpu.load[all,avg15]'),
		(29170, 10084, 'system.cpu.load[all,avg1]'),
		(29175, 10084, 'system.cpu.load[all,avg5]'),
		(29161, 10084, 'system.cpu.num'),
		(29200, 10084, 'system.cpu.util'),
		(30980, 10084, 'vfs.dev.read.await[sda]'),
		(30987, 10084, 'vfs.dev.util[sda]'),
		(30981, 10084, 'vfs.dev.write.await[sda]'),
		(29177, 10084, 'vm.memory.size[pavailable]'),
		(29178, 10084, 'vm.memory.size[total]')
	),(
		(31041, 10325, 'system.cpu.load[all,avg15]'),
		(31042, 10325, 'system.cpu.load[all,avg1]'),
		(31043, 10325, 'system.cpu.load[all,avg5]'),
		(31044, 10325, 'system.cpu.num'),
		(31073, 10325, 'system.cpu.util'),
		(31099, 10325, 'vfs.dev.read.await[sda]'),
		(31100, 10325, 'vfs.dev.read.await[sdb]'),
		(31105, 10325, 'vfs.dev.util[sda]'),
		(31106, 10325, 'vfs.dev.util[sdb]'),
		(31107, 10325, 'vfs.dev.write.await[sda]'),
		(31108, 10325, 'vfs.dev.write.await[sdb]'),
		(31070, 10325, 'vm.memory.size[pavailable]'),
		(31071, 10325, 'vm.memory.size[total]')
	), (
		(31173, 10326, 'system.cpu.util'),
		(31182, 10326, 'vm.memory.size[total]'),
		(31184, 10326, 'vm.memory.util')
	), (
		(31303, 10327, 'system.cpu.util'),
		(31312, 10327, 'vm.memory.size[total]'),
		(31314, 10327, 'vm.memory.util')
	), (
		(31422, 10328, 'system.cpu.load[all,avg15]'),
		(31423, 10328, 'system.cpu.load[all,avg1]'),
		(31424, 10328, 'system.cpu.load[all,avg5]'),
		(31425, 10328, 'system.cpu.num'),
		(31454, 10328, 'system.cpu.util'),
		(31479, 10328, 'vfs.dev.read.await[sda]'),
		(31482, 10328, 'vfs.dev.util[sda]'),
		(31483, 10328, 'vfs.dev.write.await[sda]'),
		(31451, 10328, 'vm.memory.size[pavailable]'),
		(31452, 10328, 'vm.memory.size[total]')
	), (
		(31539, 10329, 'system.cpu.load[all,avg15]'),
		(31540, 10329, 'system.cpu.load[all,avg1]'),
		(31541, 10329, 'system.cpu.load[all,avg5]'),
		(31542, 10329, 'system.cpu.num'),
		(31571, 10329, 'system.cpu.util'),
		(31624, 10329, 'vfs.dev.read.await[sda]'),
		(31627, 10329, 'vfs.dev.util[sda]'),
		(31628, 10329, 'vfs.dev.write.await[sda]'),
		(31568, 10329, 'vm.memory.size[pavailable]'),
		(31569, 10329, 'vm.memory.size[total]')),]
item_values = [(29174, 0.626006944444444), (29170, 0.6233125000000006), (29175, 0.6236666666666679), (29161, 32.0), (29200, 1.8407107423611133)]
new_item = []
for items in result:
    item2 = [items[0][1]]
    for item in items: # {'system.cpu.num': 32.0,'system.cpu.num': 32.0}

        item1 = {}
        for item_va in item_values:
            if item[0] == item_va[0]:
                item1[item[2]] = item_va[1]
                item2.append(item1)    # [10329,{'system.cpu.num': 32.0,'system.cpu.num': 32.0}]
    new_item.append(item2)
print(new_item)
