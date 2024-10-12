from flask import Flask, jsonify
from database import create_database, db
from models.meal import Meal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///daily_diet_API.db"

db.init_app(app)

@app.route("/")
def helloWorld():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    # Abrir uma sessão no banco de dados e cria-lo caso não exista.
    with app.app_context():
        create_database()

    # Executa e mantém a API ativa.
    app.run(debug=True)