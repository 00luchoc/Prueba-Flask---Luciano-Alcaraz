from flask import Flask

app = Flask(__name__)

@app.route("/Lucho")
def apodo():
    return "<p>LUCHOOO</p>"

@app.route("/Luciano")
def nombre():
    return "<p>LUCIANOOO</p>"