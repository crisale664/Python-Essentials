# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:15:07 2023

@author: CRIS-PC
"""

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")