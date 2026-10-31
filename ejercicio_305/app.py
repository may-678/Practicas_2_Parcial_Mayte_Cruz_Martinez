from flask import Flask
app=Flask(__name__)
@app.router('/')
def inicio():
    return'Hola mundo desde flask'
if __name__ =='_main_':
    app.run(debug=True)