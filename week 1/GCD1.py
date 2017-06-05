# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:31:31 2017

@author: Ashish
"""

def gcd(m,n) :
    
    for i in range(1, min(m,n)+1):
        if(m%i)==0 and (n%i)==0:
            mrcd = i
    
    return mrcd

print(gcd(10,5))
