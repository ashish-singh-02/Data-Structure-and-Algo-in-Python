# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:15:14 2017

@author: C-Ashish.Singh
"""
import getpass

class Login:
    
    def Authenticate(self):
        __UserId = input("Enter User ID : ")
        __Password = getpass.getpass("Enter Your Passwoed : ")
        if (__UserId == "Infogain" and __Password == "Info@123!"):
            return True
        else :
            return False

class User :
    objlog = Login()
    
    if(objlog.Authenticate()==True):
        print ("Login successful")
    else:
        print ("Login Fail, please try again")

    
    
