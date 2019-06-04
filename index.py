from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from product_model import Product
from extension import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def hello_world():
	test = Product.query.all()
	print("----")
	for t in test:
		print(t.id)
	print("----")
	return 'hello world!'

@app.route('/add/')
def add():
	test = Product(name="tata")
	db.session.add(test)
	db.session.commit()
	return 'user added'
