# tests/test_pedido.py

import unittest

from src.pedido import calcular_total

class TestPedido(unittest.TestCase):
    def test_un_producto_devuelve_total_correcto(self):
        productos = [
            {"nombre": "teclado", "precio": 10, "cantidad": 2}
        ]

        total = calcular_total(productos)

        self.assertEqual(total, 20)


if __name__ == "__main__":
    unittest.main()