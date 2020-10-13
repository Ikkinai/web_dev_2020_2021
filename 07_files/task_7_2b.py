# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
ignore = ["duplex", "alias", "Current configuration"]
ignoring=False 
really_that =False
f_new = open("config_sw1_cleared.txt","w")
with open(argv[1], "r") as file1:
    for line in file1:
        for i in ignore:
            for word in line.split():
                if word == i or (really_that==True and word=="configuration"):
                    ignoring =True
                else:
                    if word=="Current":
                        really_that =True
                    else: 
                        really_that =False
        if not ignoring:
            f_new.write(line.rstrip()+"\n")
        really_that =False
        ignoring =False
f_new.close()