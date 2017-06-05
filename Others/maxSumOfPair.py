# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:21:35 2017

@author: Ashish
"""

def maxSumOfPair(arr):
    l = len(arr)
    first = max(arr[0],arr[1])
    second = min(arr[0],arr[1])
    for i in range(1,l):
        if(arr[i] > first):
            second = first
            first = arr[i]
        elif((arr[i] > second) and (arr[i] < first)):
            second = arr[i]
    return (first + second)

arr= [1,2,3,4,7,90,0]
print(maxSumOfPair(arr))