persona={
    "nombre":"Suga Marry Me",
    "edad":33,
    "profesion":"Artista",
    "estudiante":False
}
print(persona)
print(persona["nombre"])
print(persona["edad"])
print(persona["profesion"])

persona["edad"]=35
print(persona.get("edad"))
#agregar un par (clave:valor)
persona["Ciudad"]="Island bts"
print(persona)
#recorrer un diccionario con un bucle
for clave,valor in persona.items():
    print(f"{clave}:{valor}")