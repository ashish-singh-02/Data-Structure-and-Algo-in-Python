# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:01:17 2017

@author: C-Ashish.Singh
"""

arr= [1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

print(arr)

count=0
for i in range(1,len(arr)):
    if(arr[i]==0):
        count=count+1
    
for j in range (1, len(arr)):
    if(j<count):
        arr[j]=0
    else:
        arr[j]=1

print(arr)
    
