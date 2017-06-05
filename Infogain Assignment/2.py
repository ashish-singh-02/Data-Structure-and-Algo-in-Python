# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:39:17 2017

@author: C-Ashish.Singh
"""


class Ticket:
    
    def Ent(self):
        
        tNum=int(input("Enter a valid Ticket Number : "))
        
        dropped=tNum%10
        newNum= (tNum-dropped)/10
        rem= newNum%7
        
        if rem == dropped  :
            return True
        else:
            return False

class Main:
    objTicket = Ticket()
    if (objTicket.Ent() == True ):
        print("Ticket Number is Valid")
    else:
        print("Invalid Ticket Number")
