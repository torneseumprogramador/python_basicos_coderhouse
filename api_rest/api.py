from flask import Flask, jsonify

app = Flask(__name__)

# Dados dos clientes fictícios
clientes = [
    {"id": 1, "nome": "Cliente 1", "telefone": "1234567890"},
    {"id": 2, "nome": "Cliente 2", "telefone": "1234567891"},
    {"id": 3, "nome": "Cliente 3", "telefone": "1234567892"},
    {"id": 4, "nome": "Cliente 4", "telefone": "1234567893"},
    {"id": 5, "nome": "Cliente 5", "telefone": "1234567894"},
    {"id": 6, "nome": "Cliente 6", "telefone": "1234567895"},
    {"id": 7, "nome": "Cliente 7", "telefone": "1234567896"},
    {"id": 8, "nome": "Cliente 8", "telefone": "1234567897"},
    {"id": 9, "nome": "Cliente 9", "telefone": "1234567898"},
    {"id": 10, "nome": "Cliente 10", "telefone": "1234567899"}
]

# Rota para obter a lista de clientes
@app.route('/clientes', methods=['GET'])
def get_clientes():
    return jsonify(clientes)

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)
