# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input("Введите ip устройства (10.1.1.0/24) ")

ip=ip.split('.')
mask= ip[3].split('/')
ip[3]=mask[0]
mask = mask[1]
ip2=ip
print("Network:")
print('{:d}\t\t{:d}\t\t{:d}\t\t{:d} '.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
print('{:08b}\t{:08b}\t{:08b}\t{:08b}'.format(int(ip2[0]),int(ip2[1]),int(ip2[2]),int(ip2[3])))

print("\nMask:")
print('/'+mask)
mask="1"*int(mask)+"0"*(32-int(mask))
mask2=ip
mask2[0]=mask[:8]
mask2[1]=mask[8:16]
mask2[2]=mask[16:24]
mask2[3]=mask[24:]

print('{:d}\t\t{:d}\t\t{:d}\t\t{:d} '.format(int(mask2[0],2),int(mask2[1],2),int(mask2[2],2),int(mask2[3],2)))
print('{:08b}\t{:08b}\t{:08b}\t{:08b}'.format(int(mask2[0],2),int(mask2[1],2),int(mask2[2],2),int(mask2[3],2)))