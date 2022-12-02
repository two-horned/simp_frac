#!/usr/bin/env python
a,b = map(int, input("Enter Fraction: ").split("/"))
def sf(a,b):
    c=a
    e=b%a
    print(e)
    while e != 0:
        d=c
        c=e
        e=d%e

    print(a/c,'/',b/c)
sf(a,b)
