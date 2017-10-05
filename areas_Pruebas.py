# -*- coding: utf-8 -*-

import unittest

from areas import areas

class areas_Pruebas(unittest.TestCase):
    def setUp(self):
        self.areas = areas()

    def test_circulo(self):
        self.areas.circulo(15)
        self.assertEquals(self.areas.obtener_resultado(),706.85834705770347865409476123789)

    def test_circulo_datosIncorrectos(self):
        self.areas.circulo('S')
        self.assertEquals(self.areas.obtener_resultado(), 'Datos incorrectos')

    def test_cuadro(self):
        self.areas.cuadro(15)
        self.assertEquals(self.areas.obtener_resultado(),225)

    def test_cuadro_datosIncorrectos(self):
        self.areas.cuadro('S')
        self.assertEquals(self.areas.obtener_resultado(), 'Datos incorrectos')

    def test_rectangulo(self):
        self.areas.rectangulo(15, 4)
        self.assertEquals(self.areas.obtener_resultado(),60)

    def test_rectangulo_datosIncorrectos(self):
        self.areas.rectangulo('S', 'u')
        self.assertEquals(self.areas.obtener_resultado(), 'Datos incorrectos')

    def test_trapecio(self):
        self.areas.trapecio(15, 4, 5)
        self.assertEquals(self.areas.obtener_resultado(),47)

    def test_trapecio_datosIncorrectos(self):
        self.areas.trapecio('S', 'u', 't')
        self.assertEquals(self.areas.obtener_resultado(), 'Datos incorrectos')


if __name__=='__main__': # pragma: nocover
    unittest.main()
