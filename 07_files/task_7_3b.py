# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan= input("Введите влан: ")
with open("07_files/CAM_table.txt", "r") as cam:
    for line in cam:
        line=line.split()
        if len(line) ==4 and line[3].startswith("Gi") and int(line[0])==int(vlan):
            print(line[0] +'\t'+line[1]+'\t  '+line[3])         
