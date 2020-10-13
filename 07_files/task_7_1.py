# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

f = open('07_files\ospf.txt', 'r')
#lines = f.readlines()

description = {
                'Prefix': 1,
                'AD/Metric': 2,
                'Next-Hop': 4,
                'Last update':5,
                'Outbound Interface':6
                }

for line in f:
    line = line.split()
    line[2]= line[2].strip("[]")
    line[4]= line[4].rstrip(",")
    line[5]= line[5].rstrip(",")
    for desc in description:
        print('{0:<20}{1:5}{2:<20}'.format(desc, ' ',str(line[description[desc]])))
    print()

f.close()
