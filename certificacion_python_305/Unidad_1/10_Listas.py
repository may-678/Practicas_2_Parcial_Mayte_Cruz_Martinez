try:
    #declarando una lista
    materias=["Programacion","Filosofia","Matematicas","Ingles","Biologia"]
    print(materias[0])
    materias.append("Lengua y Comunicacion")
    print(materias)
    materias[1]="Biologia"
    print(materias)
    materias.remove("Matematicas")
    print(materias)
except IndexError:
    print("Indice correcto")