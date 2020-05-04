import unittest

import romanos

class RomanNumberTest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(romanos.romano_a_entero('I'),1)
        self.assertEqual(romanos.romano_a_entero('V'),5)
        self.assertEqual(romanos.romano_a_entero('X'),10)
        self.assertEqual(romanos.romano_a_entero('L'),50)
        self.assertEqual(romanos.romano_a_entero('C'),100)
        self.assertEqual(romanos.romano_a_entero('D'),500)
        self.assertEqual(romanos.romano_a_entero('M'),1000)
        self.assertEqual(romanos.romano_a_entero('K'),'Error en formato')
        self.assertEqual(romanos.romano_a_entero(''),'Error en formato')

    def test_repetitions(self):
        self.assertEqual(romanos.romano_a_entero('II'),2)
        self.assertEqual(romanos.romano_a_entero('MMM'),3000)
        self.assertEqual(romanos.romano_a_entero('KK'),'Error en formato')

    def test_only_three(self):
        self.assertEqual(romanos.romano_a_entero('IIII'),'Error en formato')

    def test_digitos_decrecientes(self):
        self.assertEqual(romanos.romano_a_entero('XVIII'),18)
        self.assertEqual(romanos.romano_a_entero('IX'),9)
        #self.assertEqual(romanos.romano_a_entero('VX'),5) ## En este punto es válido, luego dará error por no ser correcto.
        self.assertEqual(romanos.romano_a_entero('XL'),40)
        #self.assertEqual(romanos.romano_a_entero('LC'),50) ## En este punto es válido, luego dará error por no ser correcto.
        self.assertEqual(romanos.romano_a_entero('CD'),400)
        #self.assertEqual(romanos.romano_a_entero('DM'),500) ## En este punto es válido, luego dará error por no ser correcto.

    def test_separacion_un_grado(self):
        self.assertEqual(romanos.romano_a_entero('XC'),90)
        self.assertEqual(romanos.romano_a_entero('XD'),'Error en formato')
        self.assertEqual(romanos.romano_a_entero('IL'),'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XM'),'Error en formato')
        self.assertEqual(romanos.romano_a_entero('VC'),'Error en formato')

    def test_resta_de_multiplos_5_NO(self):
        self.assertEqual(romanos.romano_a_entero('VC'),'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XCV'),95)

    def test_resta_un_solo_simbolo(self):
        self.assertEqual(romanos.romano_a_entero('XXL'),'Error en formato')
        self.assertEqual(romanos.romano_a_entero('IXL'),'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XXX'),30)
        


if __name__=='__main__':
    unittest.main()