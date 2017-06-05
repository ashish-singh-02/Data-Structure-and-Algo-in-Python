# -*- coding: utf-8 -*-
"""
Created on Mon May 22 23:29:30 2017

@author: Ashish
"""

def factors(n):
    factorlist = []
    for i in range(1, n+1):
        if n % i ==0:
            factorlist = factorlist + [i]
    return factorlist

def isprime(n):
    return (factors(n) == [1,n])

def nprimes(n):
    (count, i, plist) = (1, 0, [])
    while(count < n):
        if isprime(i):
            (count, plist) = (count+1, plist + [i])
        i = i + 1
    return (plist)

print(nprimes(10000))