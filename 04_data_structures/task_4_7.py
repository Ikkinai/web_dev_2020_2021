# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
mac= mac.split(':')
print(bin(int(mac[0],16))[2:]+bin(int(mac[1],16))[2:]+bin(int(mac[2],16))[2:])
