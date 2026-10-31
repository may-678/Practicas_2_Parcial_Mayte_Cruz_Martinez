from flask import Flask, render_template , request
app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def inicio():
    return render_template('index.html', mensaje='Presiona un boton.')

@app.route('/saludar', methods=['POST'])
def saludar():
     nombre= request.form['nombre']
     return render_template('index.html', mensaje=f'¡Hola{nombre}! presionaste saludar', nombre=nombre)

@app.route('/despedir', methods=['POST'])
def despedir():
     nombre= request.form['nombre']
     return render_template('index.html', mensaje=f'¡Adios{nombre}! presionaste despedir', nombre=nombre)

if __name__=='__main__':
    app.run(debug=True)