# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:32:14 2023

@author: CRIS-PC
"""

while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break