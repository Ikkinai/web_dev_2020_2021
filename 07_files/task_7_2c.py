# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv
ignore = ["duplex", "alias", "Current configuration"]
ignoring=False 
really_that =False
f_new = open(argv[2],"w")
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