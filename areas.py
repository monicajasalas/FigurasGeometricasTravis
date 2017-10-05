# -*- coding: utf-8 -*-

from math import pi

class areas():

    def __init__(self):
        self.area = 0

    def obtener_resultado(self):
        if self.area != 0:
            return self.area
        elif self.area == 0: # pragma: nocover
            return 'Datos incorrectos'


    def circulo (self,radio):
        try:
            self.area = pi * int(radio)**2
            return self.area
        except ValueError:
            self.area = 0
            return self.area

    def cuadro (self,lado):
        try:
            self.area = int(lado) * int(lado)
            return self.area
        except ValueError:
            self.area = 0
            return self.area

    def rectangulo (self, base, altura):
        try:
            self.area = int(base) * int(altura)
            return self.area
        except ValueError:
            self.area = 0
            return self.area

    def trapecio (self,baseM, base_m, altura):
        try:
            self.area = (((int(baseM) + int(base_m)) * altura) / 2)
            return self.area
        except ValueError:
            self.area = 0
            return self.area
