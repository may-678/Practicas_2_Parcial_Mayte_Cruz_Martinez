#mapa del tesoro
mapa=[
    [".",".","A","."],
    [".",".",".","."],
    [".",".",".","B"],
    [".",".",".","."]
]

filas=len(mapa)
columnas=len(mapa[0])

for i in range (filas):
    for j in range (columnas):
         if mapa[i][j]=="A":
            print(f"Tesoro encontrado en la posicion [{i},{j}]")
         if mapa[i][j]=="B":
             print(f"Tesoro encontrado en la posicion [{i},{j}]")

    
