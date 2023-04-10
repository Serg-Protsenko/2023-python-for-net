# -*- coding: utf-8 -*-
"""
Завдання 6.6a

Зробити копію скрипта завдання 6.6.

Додати перевірку введеної IP-адреси.
Адреса вважається коректно заданою, якщо вона:
- складається з 4 чисел (а не літер чи інших символів)
- числа розділені точкою
- кожне число в діапазоні від 0 до 255

Якщо адреса неправильна, виводьте повідомлення: "Wrong IP address".  Якщо
адреса правильна, перевіряти та виводити тип адреси як у завданні 6.6.

Повідомлення "Wrong IP address" має виводитися лише один раз, навіть якщо
кілька пунктів вище не виконано.


Приклад виконання скрипту:
$ python task_6_6a.py
Enter IP address: 10.10.1.1
unicast

$ python task_6_6a.py
Enter IP address: 10.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: a.a.10.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.a.a
Wrong IP address

$ python task_6_6a.py
Enter IP address: 10,1,1,1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 500.1.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.1.1.1
Wrong IP address
"""

ip_addr = input('Enter IP address: ')
ip_octs = ip_addr.split('.')
# print(ip_octs)
# print(all([0 <= int(i) <= 255 for i in ip_octs]))


if not all([i.isdigit() for i in ip_octs]) or len(ip_octs) != 4:
    print('Wrong IP address')
elif ip_addr.count('.') != 3:
    print('Wrong IP address')
elif not all([0 <= int(i) <= 255 for i in ip_octs]):
    print('Wrong IP address')
else:
    ip_first_oct = int(ip_addr.split('.')[0])
    if 1 <= ip_first_oct <= 223:
        print('unicast')
    elif 224 <= ip_first_oct <= 239:
        print('multicast')
    elif  ip_first_oct == 255:
        print('local broadcast')
    elif  ip_first_oct == 0:
        print('unassigned') 
    else:
        print('unused')
