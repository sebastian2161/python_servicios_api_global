import sqlite3
import fastavro

database_path = "instance/dataweb.db"
table_name = "departments"
avro_file_path = "backup_tablas/backup_hire.avro"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

with open(avro_file_path, "rb") as avro_file:
    avro_reader = fastavro.reader(avro_file)
    avro_schema = avro_reader.schema
    avro_data = list(avro_reader)

for row in avro_data:
    print(row)

for row in avro_data:
    insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(row))})"
    cursor.execute(insert_query, tuple(row.values()))

connection.commit()
connection.close()

print('OK')