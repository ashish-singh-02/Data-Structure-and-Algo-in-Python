# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:15:14 2017

@author: C-Ashish.Singh
"""

str = 'Hello'

print(str[0])

for i in range(0, len(str)):
    while(str[i] < str[-i]):
        (str[i], str[-i]) = (str[-i], str[i])
        i = i +1

print (str)
