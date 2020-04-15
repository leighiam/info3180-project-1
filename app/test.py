#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:07:12 2020

@author: ashleigh
"""
from datetime import date

def get_date_joined():
    today = date.today()
    date_joined = today.strftime("%B %d, %Y")
    return date_joined
    
x = get_date_joined()
print(x)
userID = 620092925

print(userID)
uid = 0
def getID():
   global userID 
   uID = userID + 1
   userID = uID

getID()
print(userID)

getID()
print(userID)
