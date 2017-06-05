# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:04:32 2017

@author: C-Ashish.Singh
"""



def fact(m):
    if m ==1 or m ==0:
        return 1
    else:
        return m*fact(m-1)
print("Enter the number")
a=int(input())    
print(fact(a))
