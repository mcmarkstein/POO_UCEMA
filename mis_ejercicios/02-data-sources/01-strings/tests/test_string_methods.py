# pylint: disable-all

import unittest
from metodos_con_strings import agregar_coma
from metodos_con_strings import pertence_a
from metodos_con_strings import cuenta_repetido
from metodos_con_strings import es_una_pregunta
from metodos_con_strings import reemplazar_una_letra
from metodos_con_strings import eliminar_espacios_exteriores
from metodos_con_strings import f_string_nombreyapellido


class TestAgregarComa(unittest.TestCase):
    def test_strings_juan_pedro_seba(self):
        """This method should return "juan, pedro, seba" """
        self.assertEqual(agregar_coma("juan pedro seba"), "juan, pedro, seba")

    def test_strings_juan_seba_pedro(self):
        """This method should return "juan, seba, pedro" """
        self.assertEqual(agregar_coma("juan seba pedro"), "juan, seba, pedro")


class TestPerteneceA(unittest.TestCase):
    def test_include_word(self):
        """This method should return True as 'hey jude' contains 'jude'"""
        self.assertEqual(pertence_a("hey jude", "jude"), True)

    def test_do_not_include_word(self):
        """This method should return False as 'hey jude' doesn't contain 'joe'"""
        self.assertEqual(pertence_a("hey jude", "joe"), False)


class TestCuentaRep(unittest.TestCase):
    def test_numbers_0_0_1_2_0_on_0(self):
        """This method should return 3"""
        self.assertEqual(cuenta_repetido("00120", "0"), 3)

    def test_numbers_0_0_1_2_0_on_3(self):
        """This method should return 0 if a_substring doesn't occur in a_string"""
        self.assertEqual(cuenta_repetido("00120", "3"), 0)


class TestEsUnaPregunta(unittest.TestCase):
    def test_es_una_pregunta(self):
        """This method should return True when a_string ends with a '?'"""
        self.assertEqual(es_una_pregunta("How are you?"), True)

    def test_is_not_a_question(self):
        """This method should return False when a_string doesn't end with a '?'"""
        self.assertEqual(es_una_pregunta("Fine."), False)


class TestWhitespace(unittest.TestCase):
    def test_leading_whitespaces(self):
        """This method should work with leading whitespaces"""
        self.assertEqual(eliminar_espacios_exteriores("  hey yo"), "hey yo")

    def test_trailing_whitespaces(self):
        """This method should work with trailing whitespaces"""
        self.assertEqual(eliminar_espacios_exteriores("hey yo  "), "hey yo")

    def test_whitespaces(self):
        """This method should work with leading and trailing whitespaces"""
        self.assertEqual(eliminar_espacios_exteriores(" hey yo  "), "hey yo")


class Testreemplazar_una_letra(unittest.TestCase):
    def test_casanova_to_cosonovo(self):
        """This method should correctly reemplazar_una_letra the letter(s) in the string"""
        self.assertEqual(reemplazar_una_letra("casanova", "a", "o"), "cosonovo")

    def test_kosovo_to_kasava(self):
        """This method should correctly reemplazar_una_letra the letter(s) in the string"""
        self.assertEqual(reemplazar_una_letra("kosovo", "o", "a"), "kasava")



class TestFString(unittest.TestCase):
    def test_john_doe_33_formatting(self):
        """Este método debe retornar "Fede Moreno tiene 33"""
        self.assertEqual(f_string_nombreyapellido("Fede", "Moreno", 33), "Fede Moreno tiene 33")
