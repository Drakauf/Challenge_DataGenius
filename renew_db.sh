#!/bin/bash

rm -rf migrations products.db
touch products.db
export FLASK_APP=index.py
flask db init
flask db migrate
flask db upgrade
