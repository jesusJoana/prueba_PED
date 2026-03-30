def calcular_total(productos):
    total = 0

    for producto in productos:
        subtotal = producto["precio"] * producto["cantidad"]
        total += subtotal

    return total
