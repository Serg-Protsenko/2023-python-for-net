# -*- coding: utf-8 -*-
"""
Завдання 5.4b

Все, як у завданні 5.4a, але, якщо користувач ввів адресу хоста, а не адресу
мережі, треба перетворити адресу хоста на адресу мережі та вивести адресу
мережі та маску, як у завданні 5.4a.

Приклад адреси мережі (усі біти хостової частини дорівнюють нулю):
* 10.0.1.0 255.255.255.0
* 190.1.0.0 255.255.0.0

Приклад адреси хоста:
* 10.0.1.1 255.255.255.0 - хост із мережі 10.0.1.0 255.255.255.0
* 10.0.5.195 255.255.255.240 - хост із мережі 10.0.5.192 255.255.255.240

Приклад роботи завдання якщо користувач ввів адресу 10.0.1.1 255.255.255.0

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Перевірити роботу скрипту на різних комбінаціях хост/маска, наприклад:
    10.0.5.195 255.255.255.240, 10.0.1.1 255.255.255.0

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Підказка: наприклад є адреса хоста у двійковому форматі та маска мережі 28.
Адреса мережі це перші 28 біт адреси хоста + 4 нуля. Тобто, наприклад, адреса
хоста 10.1.1.195/28 у двійковому форматі буде
bin_ip = "0000101000000001000000111000011"

А адреса мережі буде перших 28 символів з bin_ip + 0000 (4 тому що всього в
адресі може бути 32 біти, а 32 - 28 = 4)
00001010000000010000000111000000

#  10.0.1.1 255.255.255.0
"""

ip_str, mask_str = input('Enter network address: ').split()

mask_octets = mask_str.split('.')
mask_oct_1, mask_oct_2, mask_oct_3, mask_oct_4 = [int(i) for i in mask_octets]
mask_bin_oct_1, mask_bin_oct_2, mask_bin_oct_3, mask_bin_oct_4 = [int(bin(int(i))[2:]) for i in mask_octets]
mask_list_octs = [bin(int(i)) for i in mask_octets]

netmask = sum(bin(int(x)).count('1') for x in mask_octets)
netmask_bin = [bin(int(x)) for x in mask_octets]

ip_octets = ip_str.split('.')

mask_bin_octs = [format(int(octet), '08b') for octet in mask_octets]
ip_bin_octs = [format(int(octet), '08b') for octet in ip_octets]

bin_mask = "".join(mask_bin_octs)
bin_ip = "".join(ip_bin_octs)

net_addr = int(bin_mask, 2) & int(bin_ip, 2)
net_addr_bin = bin(net_addr)[2:].zfill(32)

net_addr_octs = [net_addr_bin[i:i+8] for i in range(0, 32, 8)]
net_addr_str = [int(octet, 2) for octet in net_addr_octs]
ip_oct_1, ip_oct_2, ip_oct_3, ip_oct_4 = net_addr_str


print(f'''
Network:
{ip_oct_1:<8}  {ip_oct_2:<8}  {ip_oct_3:<8}  {ip_oct_4:<8}
{ip_oct_1:08b}  {ip_oct_2:08b}  {ip_oct_3:08b}  {ip_oct_4:08b}''')

print(f'''
Mask:
/{netmask}
{mask_oct_1:<8}  {mask_oct_2:<8}  {mask_oct_3:<8}  {mask_oct_4:<8}
{mask_oct_1:08b}  {mask_oct_2:08b}  {mask_oct_3:08b}  {mask_oct_4:08b}''')
