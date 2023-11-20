from flask import *
from flask import jsonify
from config import config
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import Departments
from models import Jobs
from models import Hired_employees
import sqlite3
import json, requests


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
             list_control_hire.append({"id":i["id"], "name":i["name"], "datetime":i["datetime"], "department_id":i["department_id"], "job_id":i["job_id"] })
             count_3+=1

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



if __name__ == '__main__':
    app.run(port = 3000, debug=True)


