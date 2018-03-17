#!/usr/bin/env python3
def change():
    global a
    print('global a:', a)
    a = 90
    print('changed inside:', a)
a = 9

print("Before the function call ", a)
print("Inside change function", end='____')
change()
print("After the function call ", a)




