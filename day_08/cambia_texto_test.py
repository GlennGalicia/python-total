import unittest
from .cambia_texto import todo_mayusculas

class TestCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        self.assertEqual(todo_mayusculas("hola"), "HOLA")

if __name__ == "__main__":
    unittest.main()