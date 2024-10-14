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

@app.route("/meals/<int:meal_id>", methods=['PUT'])
def updateMeal(meal_id):
    data = request.get_json()
    meal = Meal.query.get(meal_id)
    if not meal:
        return jsonify({"message": "Id de refeição não encontrado"}), 404
    
    if data.get("nome") and data.get("descricao") and data.get("data_hora") and data.__contains__("data_hora"):
        meal.name = data['nome']
        meal.description = data['descricao']
        try:
            meal.datetime = datetime.strptime(data['data_hora'], "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            meal.datetime = datetime.strptime(data['data_hora'], '%d/%m/%Y %H:%M')
        meal.isDiet = data['na_dieta']

        db.session.commit()

        return jsonify({"message": f"Refeição id-{meal.id} alterada com sucesso."}), 200
    
    return jsonify({"message": "Dados informados incorretos"}), 400

@app.route("/meals/<int:meal_id>", methods=['DELETE'])
def deleteMeal(meal_id):
    meal = Meal.query.get(meal_id)
    if not meal:
        return jsonify({"message": "Id de refeição não encontrado"}), 404
    
    db.session.delete(meal)
    db.session.commit()

    return jsonify({"message": f"Refeição id-{meal.id} deletada"}), 200

if __name__ == "__main__":
    # Abrir uma sessão no banco de dados e cria-lo caso não exista.
    with app.app_context():
        create_database()

    # Executa e mantém a API ativa.
    app.run(debug=True)