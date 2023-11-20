import sqlite3
import fastavro
import io


def backup_tablas_avro(database_path, table_name, avro_file_path):
    
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    
    avro_schema = {
        "type": "record",
        "name": table_name,
        "fields": [{"name": column_name, "type": ""} for column_name in column_names]
    }
    
    if table_name=="departments":
        for i in avro_schema["fields"]:
            if i['name']=='correlativo':
                i['type']='int'
            if i['name']=='id':
                i['type']='int'
            if i['name']=='department':
                i['type']='string'

    if table_name=="jobs":
        for i in avro_schema["fields"]:
            if i['name']=='correlativo':
                i['type']='int'
            if i['name']=='id':
                i['type']='int'
            if i['name']=='job':
                i['type']='string'

    if table_name=="hired_employees":
        for i in avro_schema["fields"]:
            if i['name']=='correlativo':
                i['type']='int'
            if i['name']=='id':
                i['type']='int'
            if i['name']=='name':
                i['type']='string'
            if i['name']=='datetime':
                i['type']='string'
            if i['name']=='department_id':
                i['type']='int'
            if i['name']=='job_id':
                i['type']='int'
    
    avro_data = []
    for row in rows:
        if table_name=="hired_employees":
            if row[0]!='' and row[1]!='' and row[2]!='' and row[3]!='' and row[4]!='' and row[5]!='':
                avro_data.append({column_names[i]: value for i, value in enumerate(row)})
        else:
            avro_data.append({column_names[i]: value for i, value in enumerate(row)})
    
    try:
        with open(avro_file_path, "wb") as avro_file:
            fastavro.writer(avro_file, avro_schema, avro_data)
        connection.close()
    except:
        print("Error al escribir el archivo Avro.")

if __name__ == "__main__":
    database_path = "instance/dataweb.db"
    table_name = "departments"
    avro_file_path_departments = "backup_tablas/backup_departments.avro"

    backup_tablas_avro(database_path, table_name, avro_file_path_departments)
    print(f"Backup de la tabla '{table_name}' en formato AVRO creado en '{avro_file_path_departments}'")

    database_path = "instance/dataweb.db"
    table_name1 = "jobs"
    avro_file_path_jobs = "backup_tablas/backup_jobs.avro"

    backup_tablas_avro(database_path, table_name1, avro_file_path_jobs)
    print(f"Backup de la tabla '{table_name1}' en formato AVRO creado en '{avro_file_path_jobs}'")

    database_path = "instance/dataweb.db"
    table_name2 = "hired_employees"
    avro_file_path_hire = "backup_tablas/backup_hire.avro"

    backup_tablas_avro(database_path, table_name2, avro_file_path_hire)
    print(f"Backup de la tabla '{table_name2}' en formato AVRO creado en '{avro_file_path_hire}'")