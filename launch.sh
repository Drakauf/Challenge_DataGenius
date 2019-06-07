#!/bin/bash
source ./venv/bin/activate
export FLASK_APP=index.py
export FLASK_ENV=development
pip3 install -r requirement.txt
flask run
