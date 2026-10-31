carrito=[]
n_productos=int(input("Ingresa  el numero de productos"))
for i in range(n_productos):
    producto=input("ingresa el producto a tu carrito")
    carrito.append(producto)
print("lista creada correctamente")
print(f"tu carrito contiene {carrito}")