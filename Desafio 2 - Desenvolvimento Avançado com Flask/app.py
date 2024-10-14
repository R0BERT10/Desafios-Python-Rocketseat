from datetime import datetime
from flask import Flask, jsonify, request
from database import create_database, db
from models.meal import Meal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///daily_diet_API.db"

db.init_app(app)

@app.route("/meals", methods=['POST'])
def createNewMeal():
    data = request.get_json()
    print(data)
    if data.get("nome") and data.get("descricao") and data.get("data_hora") and data.__contains__("data_hora"):
        newMeal = Meal()
        newMeal.name = data['nome']
        newMeal.description = data['descricao']
        try:
            newMeal.datetime = datetime.strptime(data['data_hora'], "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            newMeal.datetime = datetime.strptime(data['data_hora'], '%d/%m/%Y %H:%M')

        newMeal.isDiet = data['na_dieta']

        db.session.add(newMeal)
        db.session.commit()

        return jsonify({"message": f"Refeição id-{newMeal.id} registada com sucesso."}), 201
    
    return jsonify({"message": "Dados informados incorretos"}), 400

if __name__ == "__main__":
    # Abrir uma sessão no banco de dados e cria-lo caso não exista.
    with app.app_context():
        create_database()

    # Executa e mantém a API ativa.
    app.run(debug=True)