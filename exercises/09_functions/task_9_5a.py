# -*- coding: utf-8 -*-
"""
Завдання 9.5a

Зробити копію функції generate_trunk_config із завдання 9.5

Змінити функцію таким чином, щоб вона повертала не список команд, а словник:
* ключі: імена інтерфейсів, виду 'FastEthernet0/1'
* значення: список команд, який потрібно виконати на цьому інтерфейсі

Перевірити роботу функції на прикладі словника trunk_dict та шаблону
trunk_cmd_list.


Приклад роботи функції
In [2]: pprint(generate_trunk_config(trunk_dict, trunk_cmd_list))
{'FastEthernet0/1': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 10,20,30'],
 'FastEthernet0/2': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 11,30'],
 'FastEthernet0/4': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 17']}

У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""


trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

from pprint import pprint

def generate_trunk_config(intf_vlan_dict, trunk_template):
    dict_trunk_ports = {}
    for interface, vlan in intf_vlan_dict.items():
        dict_trunk_ports[interface] = []
        for command in trunk_template:
            if 'allowed vlan' in command:
                vlan = ','.join(str(i) for i in vlan)
                command = f'{command} {vlan}'
            dict_trunk_ports[interface].append(command)
    return dict_trunk_ports
    

if __name__ == '__main__':
    pprint(generate_trunk_config(trunk_dict, trunk_cmd_list))
