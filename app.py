from flask import Flask, request, render_template, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def inicio():
    app.logger.info(f'Entramos al Path {request.path}')
    app.logger.warning('Mensaje a nivel Warning')
    app.logger.error('Mensaje a nivel Error')
    return 'Hola, Mundo desde Flask!'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos soy {nombre}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Saludos tengo {edad} años'


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)


@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('inicio'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404