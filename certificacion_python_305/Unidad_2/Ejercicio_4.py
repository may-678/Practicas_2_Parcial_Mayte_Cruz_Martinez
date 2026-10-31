promedio=[7,6,8,9,4]
#1 encontra el promedio mas bajo utilizando el ciclo for
#suponemos que el promedi mas bajo es el primer elemento
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
