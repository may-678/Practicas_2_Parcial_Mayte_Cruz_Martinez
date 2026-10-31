try:
    #Ejemplo 1 sin manejo de excepciones
    numero1=float(input("Ingresa el primer numero:"))
    numero2=float(input("Ingresa el segundo numero:"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
   print("DIVISION ENTRE CERO FALLIDA")
except ValueError:
   print("TE ESTA PIDIENDO NUMEROS")
else:
   print("EL RESULTADO ES",resultado)
finally:
   print("PROGRAMA FINALIZADO")