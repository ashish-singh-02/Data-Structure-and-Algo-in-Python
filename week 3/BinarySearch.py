# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:49:21 2017

@author: C-Ashish.Singh
"""


def binarySearch(arr,lb,ub,x):      
    if(lb <= ub ):
        mid = lb + (ub - lb) //  2
    
        if(x == arr[mid]):
            return mid
        
        elif(x > arr[ mid]):
            return binarySearch(arr, mid+1 , ub, x)
        
        elif(x < arr[ mid]):
            return binarySearch(arr, lb ,mid-1, x)
    else :
        return -1

    
arr1 = [1,2,3,4,5,6,7,8,9,10]

print(binarySearch(arr1 ,11, len(arr1)-1, 1))