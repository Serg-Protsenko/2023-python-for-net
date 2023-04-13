# -*- coding: utf-8 -*-
"""
Завдання 7.3b

Створити копію скрипта завдання 7.3a.

Переробити скрипт:
* запросити користувача ввести номер VLAN
* виводити інформацію лише за вказаним VLAN

Приклад роботи скрипта:
$ python task_7_3b.py
Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

"""

vlan_numbler = int(input('Enter VLAN number: '))
mac_list = []

with open('CAM_table.txt') as file:
    for line in file:
        if 'DYNAMIC' in line:
                line_list = line.strip().split()
                vlan = int(line_list[0])
                mac = line_list[1]
                ports = line_list[-1]
                mac_list.append([vlan, mac, ports])

mac_list.sort()
for i in mac_list:
     if i[0] == vlan_numbler:
            print(f'{i[0]:<9}{i[1]}{i[2]:>11}')
