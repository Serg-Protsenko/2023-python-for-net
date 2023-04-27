# -*- coding: utf-8 -*-
"""
Завдання 9.3

Створити функцію clean_config.

Функція clean_config повинна мати два параметри:
* config_filename - чекає як аргумент на ім'я конфігураційного файлу
* ignore_lines - чекає як аргумент на список рядків, які треба ігнорувати

Функція clean_config обробляє конфігураційний файл і повертає список команд із
зазначеного конфігураційного файлу, крім рядків конфігурації, які починаються з
'!' і рядки конфігурації, які містять рядки зі списку ignore_lines. Команди у
списку мають бути без символу нового рядка наприкінці рядка.

Перевірити роботу функції на прикладі файлу config_sw1.txt, config_sw2.txt,
config_r1.txt та списку ignore_list.

Приклад роботи функції:
In [2]: clean_config("config_r2_short.txt", ignore_list)
Out[2]:
['version 15.2',
 'hostname PE_r2',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 'ip access-list standard LDP',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 'alias configure sh do sh',
 'line con 0',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 'line aux 0',
 'line vty 0 4',
 ' login',
 ' transport input all']

In [7]: clean_config("config_r2_short.txt", ["ip", "service", "line"])
Out[7]:
['Current configuration : 4052 bytes',
 'version 15.2',
 'hostname PE_r2',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 'alias configure sh do sh',
 'alias exec ospf sh run | s ^router ospf',
 'alias exec id show int desc',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 ' login',
 ' transport input all']

In [8]: clean_config("config_r2_short.txt", ["ip", "service", "line", "alias"])
Out[8]:
['Current configuration : 4052 bytes',
 'version 15.2',
 'hostname PE_r2',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 ' login',
 ' transport input all']


У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""
from pprint import pprint

# ignore_list = ["duplex", "alias exec", "Current configuration", "service"]
ignore_list = ["ip", "service", "line"]
# ignore_list = ["ip", "service", "line", "alias"]

def clean_config(config_filename, ignore_lines):
    with open(config_filename) as file:
        clean_conf_list = []
        for line in file:
            if line.startswith('!') or any(i for i in ignore_lines if i in line):
                continue
            clean_conf_list.append(line.rstrip())
    return clean_conf_list

if __name__ == '__main__':
    config_filename = 'config_r2_short.txt'  # config_sw1.txt, config_sw2.txt, config_r1.txt та списку ignore_list 
    ignore_lines = ignore_list  # ignore_list, ["ip", "service", "line"], ["ip", "service", "line", "alias"]

    print(f'For {config_filename} it shows configuration without {ignore_lines}')
    print()
    pprint(clean_config(config_filename, ignore_lines))
    print()
