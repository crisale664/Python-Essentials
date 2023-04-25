# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:48:41 2023

@author: CRIS-PC
"""

class Neurona:
def init(self, pesos, umbrales):
self.pesos = pesos
self.umbrales = umbrales

def activacion(self, entradas):
    suma_ponderada = sum([peso * entrada for peso, entrada in zip(self.pesos, entradas)])
    salida = 1 if suma_ponderada > sum(self.umbrales) else 0
    return salida

def entrenar(self, entradas, salida_deseada, tasa_aprendizaje):
    salida_obtenida = self.activacion(entradas)
    error = salida_deseada - salida_obtenida
    for i in range(len(self.pesos)):
        self.pesos[i] += tasa_aprendizaje * error * entradas[i]
    for i in range(len(self.umbrales)):
        self.umbrales[i] += tasa_aprendizaje * error
mi_neurona = Neurona([0.5, -0.5, 1], [-0.5])

entrada = [1, 0, 1]
salida = mi_neurona.activacion(entrada)
print(f"La salida de la neurona es: {salida}")

entrada = [0, 1, 1]
salida_deseada = 0
tasa_aprendizaje = 0.1
mi_neurona.entrenar(entrada, salida_deseada, tasa_aprendizaje)

mi_neurona2 = Neurona([0.2, -0.1, 0.5, 0.3, -0.4, 0.1, -0.2, 0.4, -0.3, -0.1, -0.5, 0.2, 0.3, -0.4, 0.1, -0.3, -0.2, 0.4, 0.5, 0.1, -0.4, 0.2, -0.3, -0.5, 0.1], [0.3])

imagen_tres = [0, 0, 1, 1, 0,
0, 0, 1, 1, 0,
0, 0, 1, 1, 0,
0, 0, 1, 1, 0,
0, 0, 1, 1, 0]

mi_neurona2.entrenar(imagen_tres, 1, 0.1)

otra_imagen = [0, 0, 0, 0, 0,
0, 1, 1, 1, 0,
0, 1, 0, 1, 0,
0, 1, 1, 1, 0,
0, 0, 0, 0, 0]

salida = mi_neurona2.activacion(otra_imagen)
print(salida)