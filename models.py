from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'test'

    correlativo = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False) 
    #created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    created_at = db.Column(db.String(10), nullable=False)
    
    @classmethod
    def create(cls, usernames):
        #user = User(username=username)
        user = [User(username=username["username"], created_at=username["created_at"] ) for username in usernames]
        #return user.save()
        return User.save_all(user)
    
    def save(self):
         try:
            db.session.add(self)
            db.session.commit()
            return self
         except:
             return False
         
    @staticmethod
    def save_all(objects):
        try:
            db.session.add_all(objects)
            db.session.commit()
            return objects
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
            return False

class User1(db.Model):
    __tablename__ = 'test_nuevo'

    id_nuevo = db.Column(db.Integer, primary_key=True)
    username_nuevo = db.Column(db.String(50), nullable=False) 
    created_at_nuevo = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    @classmethod
    def create(cls, usernames):
        user1 = [User1(username_nuevo=username["username_nuevo"] ) for username in usernames]
        return User1.save_all(user1)
    
    def save(self):
         try:
            db.session.add(self)
            db.session.commit()
            return self
         except:
             return False
         
    @staticmethod
    def save_all(objects):
        try:
            db.session.add_all(objects)
            db.session.commit()
            return objects
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
            return False

# class User2(db.Model):
#     __tablename__ = 'test_cambio'

#     id_cambio = db.Column(db.Integer, primary_key=True)
#     username_cambio = db.Column(db.String(50), nullable=False) 
#     created_at_cambio = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
