from flask import Flask, url_for, render_template
import sqlite3

app = Flask(__name__)

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def AbrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory

def CerrarConexion():
    global db
    db.close()
    db = None

@app.route("/usuarios")
def usuarios():
    AbrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT usuario, id FROM usuarios ")
    res = cursor.fetchall()
    CerrarConexion()
    return render_template("ListaUsuarios.html", usuarios=res)

@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
    AbrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email, telefono, direccion FROM usuarios WHERE id = ?; ", (id,))
    res = cursor.fetchone()
    CerrarConexion()
    usuario = None
    email = None
    telefono = None
    direccion = None
    if res != None:
        usuario = res['usuario']
        email = res['email']
        telefono = res['telefono']
        direccion = res['direccion']
    return render_template("datos.html", id=id, usuario=usuario, email=email, telefono=telefono, direccion=direccion)

@app.route("/test-db")
def test08():
    AbrirConexion()
    cursor = db.cursor()
    res = cursor.execute("SELECT COUNT(*) AS cant FROM usuarios")
    registro = res.fetchone()["cant"]
    CerrarConexion()
    return f"Hay {registro} registros en la tabla usuarios"

@app.route("/")
def main():
    url_hola = url_for("hello")
    url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="img/brave_logo_stacked-1988434332.png")
    return f"""
    <a href="{url_hola}">Hola</a><br>
    <a href="{url_for('bye')}">Chau</a><br>
    <a href="{url_logo}">Logo</a><br>
    <a href="{url_dado}">Tirar dado</a>
    """

@app.route("/hola")
def hello():
    return "<p>Hola</p>"

@app.route("/chau")
def bye():
    return "<p>Chau</p>"

@app.route("/Lucho")
def apodo():
    return "<p>Lucho</p>"

@app.route("/Luciano")
def nombre():
    return "<p>Luciano</p>"

@app.route("/tirar-dado/<int:caras>")
def dado(caras):
    from random import randint
    n = randint(1, caras)
    return f"<p>Tire un dado de {caras} caras, salio {n}</p>"

