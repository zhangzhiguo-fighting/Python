#!/usr/bin/env python
# coding=utf-8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int (input("a的值是："))
b = int (input("b的值是："))

print(gcd(a, b))
