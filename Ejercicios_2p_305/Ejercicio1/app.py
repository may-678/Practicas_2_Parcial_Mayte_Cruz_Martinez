#Sirve para importar algunos modulos de la libreria Flask
from flask import Flask
#Se coloca app para que nuestro proyecto reconozca donde esta ubicado el archivo
app = Flask(__name__)
#Indica que funcion debe ejecutarse cuando alguien visita una determinada URL
@app.route('/')
#Es la funcion que se ejecutara cuando se visita la URL
def inicio():
    #Return indica que debe devolver flask al navegador
    return 'Hola mundo'
#Esta linea comprueba si se esta ejecutando directamente ese archivo en python 
if __name__=='__main__':
     #Esto inicia el servidor web de Flask
    app.run(debug=True)
