# -*- coding: utf-8 -*-
"""
Завдання 5.4a

Запросити користувача введення IP-мережі у форматі: 10.1.1.0 255.255.255.0

Потім вивести інформацію про мережу та маску в такому форматі:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Перевірити роботу скрипта на різних комбінаціях мережа/маска.

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Приклад роботи завдання:

$ python task_5_4a.py
Enter network address: 10.1.1.0 255.255.255.0

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


$ python task_5_4a.py
Enter network address: 10.1.1.192 255.255.255.240

Network:
10        1         1         192
00001010  00000001  00000001  11000000

Mask:
/28
255       255       255       240
11111111  11111111  11111111  11110000
"""
ip_str, mask_str = input('Enter network address: ').split()

ip_octets = ip_str.split('.')
ip_oct_1, ip_oct_2, ip_oct_3, ip_oct_4 = [int(i) for i in ip_octets]

mask_octets = mask_str.split('.')
mask_oct_1, mask_oct_2, mask_oct_3, mask_oct_4 = [int(i) for i in mask_octets]
netmask = sum(bin(int(x)).count('1') for x in mask_octets)

print(f'''
Network:
{ip_oct_1:<8}  {ip_oct_2:<8}  {ip_oct_3:<8}  {ip_oct_4:<8}
{ip_oct_1:08b}  {ip_oct_2:08b}  {ip_oct_3:08b}  {ip_oct_4:08b}''')

print(f'''
Mask:
/{netmask}
{mask_oct_1:<8}  {mask_oct_2:<8}  {mask_oct_3:<8}  {mask_oct_4:<8}
{mask_oct_1:08b}  {mask_oct_2:08b}  {mask_oct_3:08b}  {mask_oct_4:08b}''')

