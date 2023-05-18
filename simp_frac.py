#!/usr/bin/env python
a,b = map(int, input("Enter Fraction: ").split("/"))
def sf(a,b):
    c=b%a
    while c != 0:
        b=a
        a=c
        c=b%c
    return a
c=sf(a,b)
print(int(a/c), '/',int(b/c))
