from flask import *
from flask import jsonify
from config import config
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import Departments
from models import Jobs
from models import Hired_employees
import sqlite3
import pandas as pd
import json, requests
import logging
logging.basicConfig(filename='registro.log', level=logging.ERROR)


def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config['development']
app = create_app(enviroment)

@app.route('/api/v1/load', methods=['POST'])
def load_user():
    list_control_department=[]
    list_control_job=[]
    list_control_hire=[]
    json = request.get_json(force=True)
    #print(json)
    
    count_1=0
    for i in json[0]["departments"]:
        if count_1 < 1000:
            list_control_department.append({"id":i["id"], "department":i["department"]})
            count_1+=1

    count_2=0
    for i in json[1]["jobs"]:
         if count_2 < 1000:
             list_control_job.append({"id":i["id"], "job":i["job"] })
             count_2+=1

    count_3=0
    for i in json[2]["hired_employees"]:
         if count_3 < 1000:
             try:
                 if int(i["department_id"]) and int(i["job_id"]):
                     list_control_hire.append({"id":i["id"], "name":i["name"], "datetime":i["datetime"], "department_id":i["department_id"], "job_id":i["job_id"] })
                     count_3+=1
             except Exception as e:
                 logging.error(f"Error during transaction: {e}-Tabla hired_employees-id:{i}")
                 pass


    if len(list_control_department)>0 and len(list_control_department)<=1000:
        Departments.clean_table()
        department =  Departments.create(list_control_department)

    if len(list_control_job)>0 and len(list_control_job)<=1000:
         Jobs.clean_table()
         job = Jobs.create(list_control_job)

    if len(list_control_hire)>0 and len(list_control_hire)<=1000:
         Hired_employees.clean_table()
         hire = Hired_employees.create(list_control_hire)

    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/query1', methods=['GET'])
def load_query1():
    database_path = "instance/dataweb.db"
    lista_query1=[]
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    query ='''SELECT
        department,
        job,
        SUM(CASE WHEN quarter = 1 THEN hired_count ELSE 0 END) AS Q1,
        SUM(CASE WHEN quarter = 2 THEN hired_count ELSE 0 END) AS Q2,
        SUM(CASE WHEN quarter = 3 THEN hired_count ELSE 0 END) AS Q3,
        SUM(CASE WHEN quarter = 4 THEN hired_count ELSE 0 END) AS Q4
        FROM (SELECT department_id,
             job_id,
             COUNT(*) AS hired_count,
             STRFTIME('%Y', datetime) AS year,
        CASE
            WHEN STRFTIME('%m', datetime) BETWEEN '01' AND '03' THEN 1
            WHEN STRFTIME('%m', datetime) BETWEEN '04' AND '06' THEN 2
            WHEN STRFTIME('%m', datetime) BETWEEN '07' AND '09' THEN 3
            WHEN STRFTIME('%m', datetime) BETWEEN '10' AND '12' THEN 4
        END AS quarter
    FROM hired_employees 
    WHERE STRFTIME('%Y', datetime) = '2021'
    GROUP BY department_id,job_id,year,quarter) AS subquery, departments, jobs
	WHERE subquery.department_id = departments.id
	AND subquery.department_id = jobs.id
    GROUP BY department,
		     job
    ORDER BY department,job ASC '''
    
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()
    
    for i in rows:
        lista_query1.append({"department":i[0],"job":i[1],"Q1":i[2],"Q2":i[3],"Q3":i[4],"Q4":i[4]})
    return jsonify(lista_query1)

@app.route('/api/v1/query2', methods=['GET'])
def load_query2():
    database_path = "instance/dataweb.db"
    lista_query2=[]
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    query ='''WITH hired_employees1 AS (
              SELECT department_id,
              COUNT(*) AS hired_count
              FROM hired_employees
              WHERE STRFTIME('%Y', datetime) = '2021'
              GROUP BY department_id
              ) 
             SELECT b.id,
                    b.department,
	                a.hired_count
             FROM hired_employees1 a, departments b
             WHERE a.department_id=b.id
             AND a.hired_count > (SELECT AVG(hired_count) FROM hired_employees1)
             ORDER BY a.hired_count DESC '''
    
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()

    for i in rows:
        lista_query2.append({"id":i[0],"department":i[1],"hired":i[2]})
    return jsonify(lista_query2)



if __name__ == '__main__':
    app.run(port = 3000, debug=True)


