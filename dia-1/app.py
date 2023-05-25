from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# "postgresql://username:password@localhost:5432/dbname"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/codigo"

@app.route('/')
def index():
    return 'Hello world! 😎'

if __name__ == '__main__':
    app.run(debug=True)