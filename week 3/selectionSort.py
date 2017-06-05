# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:11:55 2017

@author: C-Ashish.Singh
"""

def selectionSort(arr):
    l = len(arr)
    for i in range(l):
        min_index = i
        
        if (arr[i] < arr[min_index]):
            min_index = i
        for j in range(i,l):
            (arr[j], arr[min_index]) = (arr[min_index], arr[j])
    return arr

arr = [9,8,7,6,5,4,1]

print(selectionSort(arr))
            