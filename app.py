from flask import Flask

app = Flask(__name__)

@app.route("/Lucho")
def apodo():
    return "<p>LUCHOOO</p>"

@app.route("/Luciano")
def nombre():
    return "<p>LUCIANOOO</p>"

@app.route("/tirar-dado/<int:caras>") 
def dado(caras):
    from random import randint 
    n = randint(1,caras)
    return f"<p>Tire un dado de {caras} caras, salio {n}</p>"