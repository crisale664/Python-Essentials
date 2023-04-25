# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:27:17 2023

@author: CRIS-PC
"""
class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"¡Hola, mi nombre es {self.nombre} y tengo {self.edad} años!")

persona1=Persona("Juan", 16)
persona2=Persona("Ana", 36)
persona1.presentarse()
persona2.presentarse()