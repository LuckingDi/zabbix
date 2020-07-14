a = (
    (31121, 'net.if.in["enp4s0f0"]'),
    (31122, 'net.if.in["enp4s0f1"]'),
    (31133, 'net.if.out["enp4s0f0"]'),
    (31041, 'system.cpu.load[all,avg15]'),
    (31042, 'system.cpu.load[all,avg1]'),
    (31043, 'system.cpu.load[all,avg5]'),
    (31044, 'system.cpu.num'), (31073, 'system.cpu.util'),
    (31099, 'vfs.dev.read.await[sda]'), (31100, 'vfs.dev.read.await[sdb]'),
    (31105, 'vfs.dev.util[sda]'), (31106, 'vfs.dev.util[sdb]'),
    (31107, 'vfs.dev.write.await[sda]'), (31108, 'vfs.dev.write.await[sdb]'),
    (31070, 'vm.memory.size[pavailable]'), (31071, 'vm.memory.size[total]'))

for i in a:
    print(i[0])