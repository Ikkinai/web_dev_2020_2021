# -*- coding: utf-8 -*-
"""
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Вывод должен быть без пустых строк.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv

with open(argv[1], "r") as file1:
    for line in file1:
        if not line.strip().startswith('!'):
            print(line.rstrip())