#!/usr/bin/env python3

import sys

in_put = sys.argv[1]
in_put_int = 0
try:
    in_put_int = int(in_put)
except ValueError:
    print("Parameter Error")
    exit()

#  Quick calculation deduction
qcd = 0
rate = 0
in_put_int = in_put_int - 3500
if in_put_int > 80000:
    rate = 0.45
    qcd = 13505
elif in_put_int >= 55000:
    rate = 0.35
    qcd = 5505
elif in_put_int >= 35000:
    rate = 0.3
    qcd = 2755
elif in_put_int >= 9000:
    rate = 0.25
    qcd = 1005
elif in_put_int >= 4500:
    rate = 0.2
    qcd = 555
elif in_put_int >= 1500:
    rate = 0.1
    qcd = 105
else:
    rate = 0.03
    qcd = 0


result = in_put_int * rate - qcd
if result <= 0:
    print("0.00")
else:
    print(format(result, ".2f"))
