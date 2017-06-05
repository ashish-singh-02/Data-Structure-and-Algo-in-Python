# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:41:53 2017

@author: Ashish
"""

def ISort(arr):
    l = len (arr)
    for i in range(l):
        while i > 0 and arr[i] <arr[i-1]:
            (arr[i] , arr[i-1]) = (arr[i-1] , arr[i])
            i = i-1
    return arr

arr = [9,8,6,4,12,5,7,4,0]

print(ISort(arr))