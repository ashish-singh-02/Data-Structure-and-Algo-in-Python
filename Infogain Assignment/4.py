# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:47:43 2017

@author: C-Ashish.Singh
"""

num = 126345678
str_num = str(num)

sum = 0

for i in range(0, 9):
    sum = sum + int(str_num[i])

for i in range(0, 9):
    sum1 = sum - int(str_num[i])
    for j in range(0 , 9):
        l=sum1%10
        if (l == int(str_num[j])):
            print("Yes :", sum1)