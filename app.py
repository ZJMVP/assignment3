import os
from math import radians, sin, cos, asin, sqrt
from flask import Flask, render_template, request
import pyodbc
import redis
import json
import pandas
import ast
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zjmvp'

azure_cache_connection_string = 'redis://:6us4QDDrYwjlHQHggSr3EVIlSUTzMHG97AzCaMdzvVI=@earthquake-assignment.redis.cache.windows.net:6379'
driver = '{ODBC Driver 18 for SQL Server}'
database = 'cse6332'
server = 'cse6322.database.windows.net'
username = "zoukuang"
password = "123456Zou"
redis_client = redis.from_url(azure_cache_connection_string)
redis_client.flushall()

with pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
    with conn.cursor() as cursor:
        temp = []
        cursor.execute("SELECT TOP 3 population, city FROM city")
        while True:
            r = cursor.fetchone()
            if not r:
                break
            print(str(r[0]) + " " + str(r[1]))
            temp.append(r)


def convert_row_to_dict(obj):
    if isinstance(obj, pyodbc.Row):
        obj_list = []
        for i in range(5):
            obj_list.append(obj[i])
        return obj_list
    return None


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/searchRange', methods=['GET', 'POST'])
def searRange():
    if request.method == 'POST':
        begin_time = datetime.datetime.now().timestamp()*1000
        Range1 = str(request.form['Range1'])
        Range2 = str(request.form['Range2'])
        r_key = 'searchRange_' + Range1 + Range2
        stored_list = redis_client.get(r_key)
        results = None
        if stored_list is None or len(stored_list) == 0:
            query = "SELECT * FROM dbo.city where population BETWEEN '" + Range1 + "' and " + Range2
            cursor.execute(query)
            results = cursor.fetchall()
            redis_client.set(r_key, json.dumps(results, default=convert_row_to_dict))
        else:
            results = json.loads(stored_list)
            print(type(results))
        end_time = datetime.datetime.now().timestamp()*1000
        return render_template("searchRange.html", length=len(results), rows=results, tims=end_time-begin_time)
    else:
        return render_template("searchRange.html")


@app.route('/searchRangeN', methods=['GET', 'POST'])
def searRangeN():
    if request.method == 'POST':
        begin_time = datetime.datetime.now().timestamp()*1000
        Range1 = str(request.form['Range1'])
        Range2 = str(request.form['Range2'])
        Num = str(request.form['Num'])
        query = "SELECT TOP " + Num + " * FROM dbo.city where population BETWEEN '" + Range1 + "' and " + Range2 + " order by NEWID()"
        cursor.execute(query)
        results = cursor.fetchall()
        end_time = datetime.datetime.now().timestamp()*1000
        return render_template("searchRangeN.html", length=len(results), rows=results, tims=end_time-begin_time)
    else:
        return render_template("searchRangeN.html")


if __name__ == '__main__':
    app.run(port=8000)
