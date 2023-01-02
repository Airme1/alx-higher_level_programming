#!/usr/bin/python3

import calculator_1

a = 10
b = 5

sumd = add(a, b)
subd = sub(a, b)
tim = mul(a, b)
divd = div(a, b)

print("{:d} + {:d} = {:d}".format(a,b,sumd))
print("{:d} + {:d} = {:d}".format(a,b,subd))
print("{:d} + {:d} = {:d}".format(a,b,tim))
print("{:d} + {:d} = {:d}".format(a,b,divd))
