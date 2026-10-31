colores=["Azul","Morado","Rojo","Amarillo","lila"]
color=input("Ingresa un color:")#rojo
encontrado=False
for contador in colores:
    print(contador)
    #Si el color actual es "Rojo", detener el bucle
    if contador==color:
        print("color encontrado! Saliendo del bucle")
        encontrado=True
        break
if not encontrado:
    print("El Color",color,"no se encontro")