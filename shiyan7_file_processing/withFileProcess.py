#!/usr/bin/env python3

#filename = '/home/shiyanlou/shiyanlou_python_louPlus/shiyan7_file_processing/test.txt'
#filename2 = '/etc/protocols'

file_name = input('Enter the file name:')

with open(file_name) as file:
    count = 0
    for line in file:
        count += 1
        print(line)
    print('Lines:', count)
    
