from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pacientes.db'
db = SQLAlchemy(app)

# Modelo de Paciente
class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    visitas = db.Column(db.String, nullable=False)

# Criação do banco de dados
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return "API de Pacientes está rodando!"

@app.route('/api/pacientes', methods=['POST'])
def adicionar_paciente():
    data = request.get_json()
    novo_paciente = Paciente(
        nome=data['nome'],
        data_nascimento=data['data_nascimento'],
        sexo=data['sexo'],
        visitas=','.join(data['visitas'])  # Armazena as visitas como uma string separada por vírgulas
    )
    db.session.add(novo_paciente)
    db.session.commit()
    return jsonify({"message": "Paciente adicionado com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
