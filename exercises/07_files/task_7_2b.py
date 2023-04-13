# -*- coding: utf-8 -*-
"""
Завдання 7.2b

Скопіювати код із завдання 7.2a та переробити його: замість виведення на стандартний потік виведення, скрипт повинен записати отримані рядки у файл.

Імена файлів потрібно передавати як аргументи скрипту:
1 аргумент ім'я вихідного конфігураційного файлу
2 аргумент ім'я підсумкового файлу конфігурації, в який будуть записані рядки

Приклад роботи завдання:
$ python task_7_2b.py config_sw1.txt new_config.txt

При цьому повинні бути відфільтровані рядки зі словами, які містяться в списку
ignore та рядки, що починаються на '!'.
"""

from sys import argv, exit

ignore = ["duplex", "alias", "configuration", "end", "service"]

if len(argv) > 2:
    file_read = argv[1]
    file_write = argv[2]

else:
    print("Потрібно передати ім'я файлу для зчитування і для запису, як аргумент командного рядка.")
    exit(1)

try:
    with open(file_read, 'r') as file, open(file_write, 'w') as new_file:
        for line in file:
            if line.startswith('!') or any(i for i in ignore if i in line):
                continue
            new_file.write(line)

except FileNotFoundError:
    print(f"Файл '{file_read}' не знайдено.")
except Exception as e:
    print(f"Помилка при обробці файлу: {e}")
