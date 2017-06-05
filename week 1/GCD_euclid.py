# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:49:32 2017

@author: Ashish
"""

def gcd(m,n):
    
    if(n>m):
        (m,n)=(n,m)
    if(m%n)==0:
        return n
    else:
        return(gcd(n,m%n))
    
print(gcd(100,120))