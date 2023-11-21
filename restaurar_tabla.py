import sqlite3
import fastavro

def restaurar_tabla_avro(database_path, table_name, avro_file_path):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    
    with open(avro_file_path, "rb") as avro_file:
        avro_reader = fastavro.reader(avro_file)
        avro_schema = avro_reader.schema
        avro_data = list(avro_reader)
    
    insert_query=f"DELETE FROM {table_name}"
    cursor.execute(insert_query)
    connection.commit()
    
    for row in avro_data:
        try:
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(row))})"
            cursor.execute(insert_query, tuple(row.values()))
        except:
            print('error insertar registro')
    
    connection.commit()
    connection.close()


if __name__ == "__main__":
    database_path = "instance/dataweb.db"

    #Seleccionar la tabla que desea cargar cambiando los parametros de entrada de la funcion
    # table_name --hired_employees, departments o jobs
    # avro_file_path --backup_hire.avro, backup_departments.avro o backup_jobs.avro
    table_name = "hired_employees"
    avro_file_path = "backup_tablas/backup_hire.avro"
    restaurar_tabla_avro(database_path, table_name, avro_file_path)
    print(f"Tabla '{table_name}' restaurada desde el archivo AVRO '{avro_file_path}'")