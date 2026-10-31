
for contador in range (0,3):
    alumnos=input("ingresa  el nombre" )
    promedio=input("ingresa el promedio")
promedio_bajo=promedio[0]
for contador in promedio:
    if contador>promedio_bajo:
        promedio_bajo=contador
print(promedio_bajo)
promedio_alto=promedio[0]
for contador in promedio:
    if contador<promedio_alto:
        promedio_alto=contador
print(promedio_alto)
