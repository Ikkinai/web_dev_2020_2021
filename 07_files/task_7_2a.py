# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ignore = ["duplex", "alias", "Current configuration"]
ignoring=False 
really_that =False
with open(argv[1], "r") as file1:
    for line in file1:
        if not line.strip().startswith('!'):
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
                print(line.rstrip())
            really_that =False
            ignoring =False
