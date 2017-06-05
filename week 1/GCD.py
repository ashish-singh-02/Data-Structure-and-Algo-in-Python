# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def gcd (m,n):
    
    if m < n:
        (m , n)=(n , m)
    
    if (m % n) == 0:
        return(n)
    else:
        return (gcd(n , m % n ))
    



a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=gcd(a,b)
print("GCD of given values is :")
print(c)
