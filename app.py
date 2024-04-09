from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def inicio():
    app.logger.info(f'Entramos al Path {request.path}')
    app.logger.warning('Mensaje a nivel Warning')
    app.logger.error('Mensaje a nivel Error')
    return 'Hola, Mundo desde Flask!'