from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__, template_folder='.')

JSON_FILE_DADOS = f"{os.getcwd()}/database/dados_armazenados.json"
JSON_FILE_DADOS_TRANSFORMADOS = f"{os.getcwd()}/database/dados_transformados.json"

@app.route("/")
def index():
    return render_template("dados.html")

@app.route("/get_dados", methods=["GET"])
def get_data():
    with open(JSON_FILE_DADOS, "r") as file:
        data = json.load(file)
    return jsonify(data)

@app.route("/get_dados_transformados", methods=["GET"])
def get_data2():
    with open(JSON_FILE_DADOS_TRANSFORMADOS, "r") as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
