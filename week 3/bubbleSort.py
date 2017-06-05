# -*- coding: utf-8 -*-
"""
Created on Wed May 31 00:34:40 2017

@author: Ashish
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0 , n-i-1):
            if(arr[j] > arr[j+1]):
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
    return arr

arr = [4,5,3,2,45,4,4,4,4,4,0,6]

print(bubbleSort(arr))