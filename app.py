from flask import Flask
from main import obtiene_peso
app = Flask(__name__)


@app.route('/')
def hello_world():
    valor = obtiene_peso()
    return valor

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)