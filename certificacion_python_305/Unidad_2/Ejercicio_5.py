carrito=[]
cantidad=int(input("¿Cuantos productos quieress agregar"))
for contador in range(cantidad):
    ptoductos=input(f"ingresa  el producto{contador+1}" )
    carrito.append(ptoductos)
print("\ntu lista de compras es :")
print(carrito)