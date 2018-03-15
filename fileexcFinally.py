#!/usr/bin/python3

filename = '/etc/protocols'
f = open(filename)
try:
    f.write("shiyanlou")
except:
    print("File write error")
finally:
    f.close()
    print("Finally file closed")
