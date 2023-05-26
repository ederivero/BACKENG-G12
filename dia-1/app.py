from flask import Flask, request
from db import db
from models.products_model import ProductsModel
from datetime import datetime

app = Flask(__name__)

# "postgresql://username:password@localhost:5432/dbname"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/codigo"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

db.init_app(app)


@app.before_request
def first_request():
    db.create_all()


@app.route('/')
def index():
    return 'Hello world! 😎'


@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        record = ProductsModel.query.all()
        response = []
        for product in record:
            response.append({
                "id": product.id,
                "name": product.name,
                "stock": product.stock,
                "price": product.price,
                "created_at": product.created_at,
                "updated_at": product.updated_at,
                "status": product.status
            })
        return {
            "message": "success",
            "data": response
        }
    elif request.method == "POST":
        json = request.json
        record = ProductsModel(
            name=json['name'],
            stock=json['stock'],
            price=json['price'],
            created_at=datetime(2012, 3, 3, 10, 10, 10),
            updated_at=datetime(2012, 3, 3, 10, 10, 10),
            status=json['status']
        )
        db.session.add(record)
        db.session.commit()
        return {
            "message": "success",
            "data":  {
                "id": record.id,
                "name": record.name,
                "stock": record.stock,
                "price": record.price,
                "created_at": record.created_at,
                "updated_at": record.updated_at,
                "status": record.status
            }
        }, 200


if __name__ == '__main__':
    app.run(debug=True)
