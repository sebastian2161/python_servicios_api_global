import csv
import json


archivo_csv = 'archivos_cargas/departments.csv'
archivo_csv1= 'archivos_cargas/jobs.csv'
archivo_csv2= 'archivos_cargas/hired_employees.csv'


lista_departments = []
lista_jobs = []
lista_hire= []

with open(archivo_csv, newline='', encoding='utf-8') as archivo:
    lector_csv = csv.reader(archivo)
    
    for fila in lector_csv:
        
        lista_departments.append({"id":int(fila[0]),"department":str(fila[1])})

with open(archivo_csv1, newline='', encoding='utf-8') as archivo1:
    lector_csv = csv.reader(archivo1)
    
    for fila in lector_csv:
        
        lista_jobs.append({"id":int(fila[0]),"job":str(fila[1])})

with open(archivo_csv2, newline='', encoding='utf-8') as archivo2:
    lector_csv = csv.reader(archivo2)
    
    for fila in lector_csv:
        
        if fila[3]!='':
            fila[3]=int(fila[3])

        if fila[4]!='':
            fila[4]=int(fila[4])

        lista_hire.append({"id":int(fila[0]),"name":str(fila[1]),"datetime":str(fila[2]),"department_id":fila[3], "job_id":fila[4]  })

estructura_datos_postman=[
    {"departments":lista_departments},
    {"jobs":lista_jobs},
    {"hired_employees":lista_hire} 
]

# Convertir a formato JSON
estructura_datos_postman = json.dumps(estructura_datos_postman, indent=1)

nombre_archivo = "estructura_datos_postman.json"
with open(nombre_archivo, 'w') as archivo:
    archivo.write(estructura_datos_postman)




