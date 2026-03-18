# src/pedido.py

def calcular_total(productos):
    total = 0

    for producto in productos:
        total += producto["precio"] * producto["cantidad"]

    return total
