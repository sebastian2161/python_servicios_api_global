from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.sql import text
import logging

db = SQLAlchemy()
logging.basicConfig(filename='registro.log', level=logging.ERROR)

class Departments(db.Model):
    __tablename__ = 'departments'

    correlativo = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(50), nullable=False) 

    @classmethod
    def create(cls, departments):
        department = [Departments(id=department["id"],department=department["department"] ) for department in departments]
        return Departments.save_all(department)
    
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
            logging.error(f"Error during transaction: {e}")
            return False
        
    def clean_table():
        try:
            db.session.query(Departments).delete()
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False



class Jobs(db.Model):
    __tablename__ = 'jobs'

    correlativo = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String(50), nullable=False) 

    @classmethod
    def create(cls, jobs):
        job = [Jobs(id=job["id"],job=job["job"] ) for job in jobs]
        return Jobs.save_all(job)
    
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
            logging.error(f"Error during transaction: {e}")
            return False
        
    def clean_table():
        try:
            db.session.query(Jobs).delete()
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False
        


class Hired_employees(db.Model):
    __tablename__ = 'hired_employees'

    correlativo = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.String(20), nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    job_id = db.Column(db.Integer, nullable=False) 

    # Restricción CHECK para asegurar sea un valor entero
    __table_args__ = (
        CheckConstraint('typeof(department_id) = "integer"', name='check_department_id_integer'),
        CheckConstraint('typeof(job_id) = "integer"', name='check_job_id_integer')
    )
    

    @classmethod
    def create(cls, hired_employees):
        hired_employee = [Hired_employees(id=hired_employee["id"],
                                          name=hired_employee["name"],
                                          datetime=hired_employee["datetime"],
                                          department_id=hired_employee["department_id"],
                                          job_id=hired_employee["job_id"] ) for hired_employee in hired_employees]                                
        return Hired_employees.save_all(hired_employee)
    
    def save(self):
        try:
            for i in self:
                try:
                    db.session.add(i)
                except Exception as e:
                    logging.error(f"Error during transaction: {e}")
                    return False
                db.session.commit()
            return self
        except Exception as e:
            logging.error(f"Error during transaction: {e}")
            return False
         
    @staticmethod
    def save_all(objects):
        try:
            db.session.add_all(objects)
            db.session.commit()
            return objects
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error during transaction: {e}")
            return False
    
    def clean_table():
        try:
            db.session.query(Hired_employees).delete()
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False
