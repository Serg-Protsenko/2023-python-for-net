# -*- coding: utf-8 -*-
"""
Завдання 4.3

Отримати з рядка config такий список VLANів:
['1', '3', '10', '20', '30', '100']

Записати список у змінну result (саме ця змінна перевірятиметься у тесті).

Отриманий список результату вивести на стандартний потік виведення (stdout) за
допомогою print. Тут дуже важливий момент, що треба отримати саме список (тип
даних), а не, наприклад, рядок, який схожий візуально на показаний список.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlan_item = config.split()
# result = [item.split(',') for item in vlan_item if any(char.isdigit() for char in item)]
for item in vlan_item:
    if any(char.isdigit() for char in item):
        result = item.split(',')
print(result)
