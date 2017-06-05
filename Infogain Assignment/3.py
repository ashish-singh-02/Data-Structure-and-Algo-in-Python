# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:16:15 2017

@author: C-Ashish.Singh
"""

class Day:
                
    def DayOfWeek(self):
        Date= input("Enter the date in fromat : MM/DD/YYYY")
        
        M = Date[0 : 2]
        D = Date[3 : 5]
        Y = Date[6 : 10]
        
        if(M >= 3):
            m = M - 2
        else:
            m = M + 10
        
        A= int(13 * m - 1)
        B = int(YYYY / 4)
        
        
class Main:
    obj1= Day()
    obj1.DayOfWeek()