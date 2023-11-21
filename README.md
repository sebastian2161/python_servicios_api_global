# Python_Servicios_API_Globant
 Desarrollo de servicios end-point

Paso 1: Deben ejecutar la funcionalidad formato_csv_json.py, para crear el archivo estructura_datos_postman.json. El archivo json debe cargarse en la Plataforma Postman y realizar la configuracion con el metodo POST - http://127.0.0.1:3000/api/v1/load. Este archivo json es creado utilizando los archivos.csv departments, jobs y hired_employees.

Paso 2: Luego deben ejecutar la funcionalidad main.py, para desplegar el servidor web de Flask, para poder utilizar los servicios end-point.

Paso 3: Luego de haber realizado los pasos anteriores. Deben volver a la Plataforma Postman, para ejecutar el servicio end-point http://127.0.0.1:3000/api/v1/load y cargar las tablas departments, jobs y hired_employees en la base de datos dataweb.db en Sqlite portable. 

Paso 4: Una vez creadas las tablas mencionadas, la funcionalidad backup_tablas.py estara disponible, para respaldarlas en el formato avro, en la carpeta backup_tablas.

Paso 5: Luego de tener las tablas en archivos avro, la funcionalidad restaurar_tabla.py estara disponible, para restaurarlas en la base de datos dataweb.db en Sqlite portable.

Paso 6: Las funcionalidades para las consultas de los siguientes servicios end-point estan disponibles. 
metodo GET - http://127.0.0.1:3000/api/v1/query1, obtiene por trimestre la cantidad de empleados contratados por departaments y job del año 2021.
metodo GET - http://127.0.0.1:3000/api/v1/query2, obtiene la cantidad de empleados contratados por departaments que son mayores al promedio de contrataciones del año 2021.


# Especificaciones Tecnicas
El desarrollo de los servicios endpoint, las funcionalidades de transformacion de formato, backup en archivos avro y restauracion de tablas, fueron en el sistema operativa windows 10.

La version de python utilizada fue 3.9, en un entorno virtual utilizando los siguientes pasos:
    --Crea un directorio para el entorno virtual 
    mkdir venv
    
    --Entrar al directorio del entorno virtual
    cd venv

    --Crea el entorno virtual
     python -m venv myenv


