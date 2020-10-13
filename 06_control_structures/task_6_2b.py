# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите ip ")
ip= ip.split('.')

while len(ip)!=4:
    print("Неправильный IP-адрес")
    ip = input("Введите ip ")
    ip= ip.split('.')
else:
    while not(0<=int(ip[0])<=255 or 0<=int(ip[1])<=255 or 0<=int(ip[2])<=255 or 0<=int(ip[3])<=255):
        print("Неправильный IP-адрес")
        ip = input("Введите ip ")
        ip= ip.split('.')
ip[0]=int(ip[0])
ip[1]=int(ip[1])
ip[2]=int(ip[2])
ip[3]=int(ip[3])
if ip[0]<=223 and ip[0]>0:
    res="unicast"
elif ip[0]<=239 and ip[0]>=224:
    res="multicast"
elif ip[0]==ip[1]==ip[2]==ip[3]==255:
    res="local broadcast"
elif ip[0]==ip[1]==ip[2]==ip[3]==0:
    res="unassigned"
else:
    res="unused"
print(res)