import unittest
from app.scripts.charfun import esPalindromo
import random
import string

def generar_palindromo():
    """
    Genera un palíndromo aleatorio.
    """
    mitad = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))
    return mitad + mitad[::-1]

def generar_no_palindromo():
    """
    Genera una cadena aleatoria que no es un palíndromo.
    """
    while True:
        cadena = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 20)))
        if cadena != cadena[::-1]:  # Verifica que no sea un palíndromo
            return cadena

class TestEsPalindromo(unittest.TestCase):

    def test_palindromo_simple(self):
        self.assertTrue(esPalindromo("anilina"))

    def test_palindromo_con_espacios(self):
        self.assertTrue(esPalindromo("Amo la paloma"))

    def test_palindromo_con_mayusculas(self):
        self.assertTrue(esPalindromo("A Santa At nasa"))

    def esPalindromo(cadena):
        """
        Función que verifica si una cadena es palíndroma.
        Ignora espacios, mayúsculas y tildes.
        """
        # Normalizar la cadena para eliminar acentos y otros diacríticos
        cadena_normalizada = unicodedata.normalize('NFD', cadena)
        cadena_sin_tildes = ''.join(
            char for char in cadena_normalizada if unicodedata.category(char) != 'Mn'
        )
        
        # Convertir la cadena a minúsculas y eliminar caracteres no alfanuméricos
        cadena_limpia = ''.join(
            char.lower() for char in cadena_sin_tildes if char.isalnum()
        )
        
        # Comparar la cadena limpia con su reverso
        return cadena_limpia == cadena_limpia[::-1]

    def test_no_palindromo(self):
        self.assertFalse(esPalindromo("Esto no es un palíndromo"))

    def test_cadena_vacia(self):
        self.assertTrue(esPalindromo(""))

    def test_solo_caracteres_no_alfanumericos(self):
        self.assertTrue(esPalindromo("...,,,;;;"))

    def test_numeros_palindromos(self):
        self.assertTrue(esPalindromo("12321"))

    def test_numeros_no_palindromos(self):
        self.assertFalse(esPalindromo("12345"))

    def test_palindromos_aleatorios(self):
        for _ in range(10):  # Genera y prueba 10 palíndromos aleatorios
            cadena = generar_palindromo()
            print(f"Probando palíndromo aleatorio: {cadena}")
            self.assertTrue(esPalindromo(cadena))

    def test_no_palindromos_aleatorios(self):
        for _ in range(10):  # Genera y prueba 10 no-palíndromos aleatorios
            cadena = generar_no_palindromo()
            print(f"Probando no-palíndromo aleatorio: {cadena}")
            self.assertFalse(esPalindromo(cadena))

if __name__ == "__main__":
    unittest.main()
