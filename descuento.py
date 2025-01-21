precio_original = int(input("Digite el precio del producto: "))
descuento = precio_original * (1 - 10 / 100)

if precio_original > 100:
    print("El precio con descuento es", descuento)
    