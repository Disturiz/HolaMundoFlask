from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = 'Mi_llave_secreta'


@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ha hecho Login {session["username"]}'
    return 'No ha hecho Login!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Omitimos validación del usuario
        usuario = request.form['username']
        # Agregar el usuario a la sesión
        # session['username'] = usuario
        session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))


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


# REST Representational State Transfer
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method}
    return jsonify(valores)
