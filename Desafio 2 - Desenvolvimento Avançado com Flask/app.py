from flask import Flask, jsonify
from database import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

@app.route("/")
def helloWorld():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.run(debug=True)