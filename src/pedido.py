# src/pedido.py

def calcular_total(productos):
    producto = productos[0]
    return producto["precio"] * producto["cantidad"]
