# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:34:43 2023

@author: CRIS-PC
"""

def cumplir_anios(self):
self.edad += 1
print(f"¡Feliz cumpleaños! Ahora tengo {self.edad} años.")

def cambiar_nombre(self, nuevo_nombre):
    self.nombre = nuevo_nombre
    print(f"Mi nombre ha sido cambiado a {self.nombre}.")
    
def es_mayor_de_edad(self):
    if self.edad >= 18:
        return True
    else:
        return False