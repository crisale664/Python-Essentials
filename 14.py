# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:22:25 2023

@author: Juan Carlos
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"¡Hola, mi nombre es {self.nombre} y tengo {self.edad} años!")
        
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
persona1=Persona("Juan", 16)
persona2=Persona("Ana", 36)
persona1.presentarse()
persona2.presentarse()
persona1.cumplir_anios()
persona1.cambiar_nombre("Juan Carlos")
persona1.es_mayor_de_edad()
persona2.cumplir_anios()
persona2.cambiar_nombre("Ana Maria")
persona2.es_mayor_de_edad()