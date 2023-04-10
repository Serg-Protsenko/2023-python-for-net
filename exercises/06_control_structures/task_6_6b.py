# -*- coding: utf-8 -*-
"""
Завдання 6.6b

Зробити копію скрипта завдання 6.6a.
Доповнити скрипт: якщо адреса була введена неправильно, запитати адресу знову.

Якщо адреса неправильна, виводьте повідомлення: 'Wrong IP address'.
Повідомлення "Wrong IP address" має виводитися лише один раз після кожного
введення адреси, навіть якщо кілька пунктів перевірки адреси не виконано
(приклад виведення нижче).

Приклад виконання скрипту:
$ python task_6_6b.py
Enter IP address: 10.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: a.a.a
Wrong IP address
Enter IP address: 10.1.1.1.1
Wrong IP address
Enter IP address: 500.1.1.1
Wrong IP address
Enter IP address: a.1.1.1
Wrong IP address
Enter IP address: 50.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: 10.a.1.1.1
Wrong IP address
Enter IP address: 255.255.255.255
local broadcast

"""

while True:
    ip_addr = input('Enter IP address: ')
    ip_octs = ip_addr.split('.')

    if not all([i.isdigit() for i in ip_octs]) or len(ip_octs) != 4:
        print('Wrong IP address')
        continue
    elif ip_addr.count('.') != 3:
        print('Wrong IP address')
        continue
    elif not all([0 <= int(i) <= 255 for i in ip_octs]):
        print('Wrong IP address')
        continue
    else:
        ip_first_oct = int(ip_addr.split('.')[0])
        if 1 <= ip_first_oct <= 223:
            print('unicast')
            break
        elif 224 <= ip_first_oct <= 239:
            print('multicast')
            break
        elif  ip_first_oct == 255:
            print('local broadcast')
            break
        elif  ip_first_oct == 0:
            print('unassigned')
            break
        else:
            print('unused')
            break
