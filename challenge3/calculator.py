#!/usr/bin/env python3

import os
import csv
import sys
#list = []
#dict = {}
#for arg in sys.argv[1:]:
#    try:
#        list.append(arg.split(':')[0])
#        dict[arg.split(':')[0]] = int(arg.split(':')[1])
#    except ValueError:
#        print("Parameter Error")
#
#def getPostTaxWage(wage):
#    qcd = 0
#    rate = 0
#    wage_tax_val = wage - wage * (0.08 + 0.02 + 0.005 + 0.06) - 3500
#    if wage_tax_val > 80000:
#        rate = 0.45
#        qcd = 13505
#    elif wage_tax_val >= 55000:
#        rate = 0.35
#        qcd = 5505
#    elif wage_tax_val >= 35000:
#        rate = 0.3
#        qcd = 2755
#    elif wage_tax_val >= 9000:
#        rate = 0.25
#        qcd = 1005
#    elif wage_tax_val >= 4500:
#        rate = 0.2
#        qcd = 555
#    elif wage_tax_val >= 1500:
#        rate = 0.1
#        qcd = 105
#    else:
#        rate = 0.03
#        qcd = 0
#
#    tax = wage_tax_val * rate - qcd
#    if tax <= 0:
#        return wage - wage * (0.08 + 0.02 + 0.005 + 0.06) 
#    else:
#        return wage - tax - wage * (0.08 + 0.02 + 0.005 + 0.06) 
#
#for k in list:
#    print(k+':'+format(getPostTaxWage(dict[k]), ".2f"))


class Args(object):
    def __init__(self):
        self.args = self._read_args()
    def _read_args(self):
        if sys.argv[1] != '-c':
            raise Exception('-c')
        elif os.path.isfile(sys.argv[2]) == False:
            raise Exception(sys.argv[2],'config is not right')
        elif sys.argv[3] != '-d':
            raise Exception('-d')
        elif os.path.isfile(sys.argv[4]) == False:
            raise Exception('data is not right')
#        elif os.path.exists(sys.argv[5][0:sys.len(sys.argv[5])-])


def main():
    print(sys.argv)

if __name__ == '__main__':
    main()











