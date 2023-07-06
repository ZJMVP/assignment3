import os
from math import radians, sin, cos, asin, sqrt
from flask import Flask, render_template, request
import pyodbc
import redis
import json
import pandas
import ast

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zjmvp'


def convert_row_to_dict(obj):
    if isinstance(obj, pyodbc.Row):
        obj_list = []
        for i in range(22):
            obj_list.append(obj[i])
        return obj_list
    return None


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/passwordValidator", methods=['GET', 'POST'])
def password_validator():
    return render_template('passwordValidator.html')


@app.route("/textValidatorCheckor", methods=['GET', 'POST'])
def text_validator_checkor():
    return render_template('textValidatorCheckor.html')


if __name__ == '__main__':
    app.run(port=8000)
