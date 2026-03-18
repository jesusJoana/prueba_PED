# src/pedido.py

def calcular_total(productos):
    total = 0

    for producto in productos:
        if producto["cantidad"] <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        subtotal = producto["precio"] * producto["cantidad"]
        total += subtotal

    return total

