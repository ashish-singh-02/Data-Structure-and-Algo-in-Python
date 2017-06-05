# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:25:04 2017

@author: C-Ashish.Singh
"""



def linearSearch(x, data):
    pos = -1
    for i in range(0, len(data)):
        if data[i]== x:
            return i
    return pos
        


data = [4,5,6,3,2,5,7,99,21,67,33,90,32,68,3435,0,11,1]

print(linearSearch(11, data))