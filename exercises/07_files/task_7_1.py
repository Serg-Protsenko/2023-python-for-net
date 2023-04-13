# -*- coding: utf-8 -*-
"""
Завдання 7.1

Обробити рядки з файлу ospf.txt і вивести інформацію щодо кожного рядка в
такому вигляді на стандартний потік виводу:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

"""

ip_info = {}

with open('ospf.txt') as f:
    for line in f:
        line_list = line.rstrip().split()
        prefix = line_list[1]
        metric = line_list[2].strip('[]')
        next_hop = line_list[4].strip(',')
        update = line_list[5].strip(',')
        interface = line_list[-1]
        
        sample = f'''
Prefix                {prefix}
AD/Metric             {metric}
Next-Hop              {next_hop}
Last update           {update}
Outbound Interface    {interface}'''
        print(sample)
