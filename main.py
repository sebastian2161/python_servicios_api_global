from flask import *
from flask import jsonify
from config import config
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import User
from models import User1
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

# @app.route('/api/v1/connect', methods=['GET'])
# def connect_db():
#     con = sqlite3.connect('instance/dataweb.db')
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM test") 
#     data= cursor.fetchall()
#     response = {'message': data}
#     return jsonify(response)


# @app.route('/api/v1/users', methods=['GET'])
# def get_users():
#     response = {'message': 'success'}
#     return jsonify(response)


@app.route('/api/v1/load', methods=['POST'])
def load_user():
    list_control_users=[]
    list_control_users1=[]
    json = request.get_json(force=True)
    print(json)
    
    count_1=0
    for i in json[0]["users"]:
        if count_1 <=1000:
            list_control_users.append({"username":i["username"], "created_at":i["created_at"]})
            count_1+=1

    count_2=0
    for i in json[1]["users1"]:
        if count_2 <=1000:
            list_control_users1.append({"username_nuevo":i["tipo_house"]})
            count_2+=1

    #if json.get('username') is None:
    #    return jsonify({'message': 'Bad request'})
    #user = User.create(json['username'])

    if len(list_control_users)>0 and len(list_control_users)<=1000:
        user =  User.create(list_control_users)

    if len(list_control_users1)>0 and len(list_control_users1)<=1000:
        user1 =  User1.create(list_control_users1)

    return jsonify({'user': json})



if __name__ == '__main__':
    app.run(port = 3000, debug=True)


