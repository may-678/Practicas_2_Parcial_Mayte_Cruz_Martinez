inventario = {"lapiz": 10, "cuaderno": 5, "borrador": 8}

producto = input("Producto: ").lower()
cantidad = int(input("Cantidad: "))

if producto in inventario:
    if cantidad <= 0:
        print("Cantidad debe ser positiva")
    elif cantidad > inventario[producto]:
        print("No hay suficiente")
    else:
        inventario[producto] -= cantidad
        print("Vendido. Quedan:", inventario[producto])
else:
    print("No existe")