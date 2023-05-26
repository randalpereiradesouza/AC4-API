from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/listar', methods=['GET'])
def listar():
    response = requests.get('http://127.0.0.1:5000/consultar')
    data = response.json()
    return jsonify(data)


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']

    if nome is None or sobrenome is None or cpf is None:
        return jsonify({'error': 'Dados incompletos'})

    clientes = {
        'nome': nome,
        'sobrenome': sobrenome,
        'cpf': cpf
    }

    response = requests.post('http://127.0.0.1:5000/cadastrar', data=clientes)
    data = response.json()

    return jsonify(data)


@app.route('/deletar', methods=['DELETE'])
def deletar():
    parametro = request.form['parametro']
    valor = request.form['valor']

    if parametro is None or valor is None:
        return jsonify({'error': 'Dados incompletos'})

    dados = {
        'parametro': parametro,
        'valor': valor
    }

    response = requests.delete('http://127.0.0.1:5000/deletar', data=dados)
    data = response.json()

    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5001)
