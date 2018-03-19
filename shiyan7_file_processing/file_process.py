#!/usr/bin/env python3

filename = '/home/shiyanlou/test.txt'
#file = open(filename)
#s = file.read()
#print(s)
#file.close()

#with open(filename) as file:
#    print(file.read())


file = open(filename)
print(file.readline())
print(file.readline())
file.close()
file = open(filename)
print(file.readlines())
file.close()
