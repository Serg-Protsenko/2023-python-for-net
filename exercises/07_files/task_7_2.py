# -*- coding: utf-8 -*-
"""
Завдання 7.2

Створити скрипт, який оброблятиме конфігураційний файл комутатора і виводити на
екран рядки з конфіга, крім деяких.

Ім'я конфігураційного файлу передається як аргумент скрипту:
$ python task_7_2.py config_sw1.txt

Вивести на стандартний потік виведення команди з переданого конфігураційного
файлу, крім рядків, які починаються з '!'.

Вивід має бути без порожніх рядків.

Приклад роботи завдання:
$ python task_7_2.py config_sw1.txt
Current configuration : 2033 bytes
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
 duplex auto
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 duplex auto
 spanning-tree portfast edge trunk
interface Ethernet0/2
 duplex auto
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 duplex auto
 switchport mode trunk
 spanning-tree portfast edge trunk
...

"""
from sys import argv, exit

if len(argv) > 1:
    file_name = argv[1]
else:
    print("Потрібно передати ім'я файлу як аргумент командного рядка.")
    exit(1)

try:
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith('!'):
                continue
            print(line, end='')

except FileNotFoundError:
    print(f"Файл '{file_name}' не знайдено.")
except Exception as e:
    print(f"Помилка при обробці файлу: {e}")
