nuevo_usuario={}
#pedimos datos desde el teclado
nuevo_usuario["Nombre"]=input("Ingresa tu nombre")
nuevo_usuario["Edad"]=int(input("Ingresa tu edad"))
nuevo_usuario["Estatura"]=float(input("Ingresa tu estatura en m"))
nuevo_usuario["Rol"]=input("Ingresa tu  rol en BtS")
nuevo_usuario["Signo Zodiacal"]=input("Ingresa tu signo zodiacal")
print("\n ---Informacion guardada---")
#mostrando la informacion del diccionario
print(nuevo_usuario)