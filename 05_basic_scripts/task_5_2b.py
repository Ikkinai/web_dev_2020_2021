# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ip=argv[1].split('.')
mask= ip[3].split('/')
ip[3]=0
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