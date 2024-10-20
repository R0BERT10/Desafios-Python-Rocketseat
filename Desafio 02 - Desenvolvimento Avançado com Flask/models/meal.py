from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import mapped_column
from database import db

class Meal(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    description = mapped_column(String, nullable=False)
    datetime = mapped_column(DateTime, nullable=False)
    isDiet = mapped_column(Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.name,
            "descricao": self.description,
            "data_hora": self.datetime.strftime("%Y-%m-%d %H:%M"),
            "na_dieta": self.isDiet
        }
