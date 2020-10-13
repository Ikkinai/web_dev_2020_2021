# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите ip ")
ip= ip.split('.')
if int(ip[0])<=223 and int(ip[0])>0:
    res="unicast"
elif int(ip[0])<=239 and int(ip[0])>=224:
    res="multicast"
elif int(ip[0])==int(ip[1])==int(ip[2])==int(ip[3])==255:
    res="local broadcast"
elif int(ip[0])==int(ip[1])==int(ip[2])==int(ip[3])==0:
    res="unassigned"
else:
    res="unused"
print(res)