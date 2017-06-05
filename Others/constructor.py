# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:14:43 2017

@author: Ashish
"""

class Person:
    def __init__(self,name):
        self.name = name
    
    def say_hi(self):
        print('hello, my name is ', self.name)
        
p= Person('Ashish')
p.say_hi()
