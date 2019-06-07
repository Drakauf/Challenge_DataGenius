from flask import Flask, request, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from product_model import Product
from extension import db
import json
import query

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    test = Product.query.all()
    return render_template('index.html', products=test)


@app.route('/add/')
def add():
    return query.setup()

@app.route('/add_product/', methods=['POST'])
def add_product():
    return query.add_product(request.json)


@app.route('/calculate/', methods=['POST'])
def calculate():
    products = json.loads(request.form['form_text'])
    ret = query.calculate(products)
    return render_template('result.html', pannier=ret)
