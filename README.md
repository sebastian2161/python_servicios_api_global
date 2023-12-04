# Python_Services_API_Globant
 Development of endpoint services

Step 1: You must execute the formatting_csv_json.py functionality to create the structure_data_postman.json file. The json file must be uploaded to the Postman Platform and configured with the POST method - http://127.0.0.1:3000/api/v1/load . This json file is created using the departments, jobs and hired_employees.csv files.

Step 2: Then they must execute the main.py functionality, to deploy the Flask web server, in order to use the endpoint services.

Step 3: After having completed the previous steps. They must return to the Postman Platform to run the endpoint service http://127.0.0.1:3000/api/v1/load and load the departments, jobs and hired_employees tables in the dataweb.db database in Sqlite portable. 

Step 4: Once the aforementioned tables have been created, the backup_tablas.py functionality will be available to backup them in the avro format, in the backup_tablas folder.

Step 5: After having the tables in avro files, the restore_tabla.py functionality will be available to restore them to the dataweb.db database in Sqlite portable.

Step 6: The functionalities for queries of the following endpoint services are available. GET method - http://127.0.0.1:3000/api/v1/query1 , obtains per quarter the number of employees hired by departments and jobs for the year 2021. GET method - http://127.0.0.1:3000/api/ v1/query2 , obtains the number of employees hired by departments that are greater than the average hiring for the year 2021.


# Technical specifications
The development of the endpoint services, the format transformation functionalities, backup in avro files and restoration of tables, were in the Windows 10 operating system.

The python version used was 3.9, in a virtual environment using the following steps:

    --Create a directory for the virtual environment
    mkdir venv
    
    --Enter the virtual environment directory
    cd venv

    --Create the virtual environment
     python -m venv myenv

The requirements file with the list of libraries was created

    --pip freeze > requirements.txt
       blinker==1.7.0
       certifi==2023.11.17
       charset-normalizer==3.3.2
       click==8.1.7
       colorama==0.4.6
       fastavro==1.9.0
       flask==3.0.0
       flask-sqlalchemy==3.1.1
       greenlet==3.0.1
       idna==3.4
       importlib-metadata==6.8.0
       itsdangerous==2.1.2
       Jinja2==3.1.2
       MarkupSafe==2.1.3
       numpy==1.26.2
       pandas==2.1.3
       python-dateutil==2.8.2
       pytz==2023.3.post1
       requests==2.31.0
       six==1.16.0
       SQLAlchemy==2.0.23
       typing-extensions==4.8.0
       tzdata==2023.3
       urllib3==2.1.0
       werkzeug==3.0.1
       zipp==3.17.0

To carry out the simulation and testing of the endpoint services, the postman api platform (cloud) was used, link: https://www.postman.com/ , you must have an account created to access all the functionalities. To configure the POST Method you must select Body-->raw-->json
       
The database used was the local version of SQLite and in the cloud. The cloud version is created with a google chrome web store extension, link: https://chromewebstore.google.com/detail/sqlite-viewer/bpedjnknnoaegoaejefbodcdjmjkbbea?hl=es&pli=1

--Step 1: You must add extension

--Step 2: You must upload the dataweb.db database located in the instance folder, click to load from your hard drive

--Step 3: Paste the following query into the text editor to list the database tables.

     --Querys 
         SELECT `name`, `sql`
         FROM `sqlite_master`
         WHERE type='table';

         SELECT * FROM departments
         SELECT * FROM jobs
         SELECT * FROM hired_employees

This alternative or option is to review the results of the SQLite database tables in the cloud

NOTE: The main branch is the one with the latest changes https://github.com/sebastian2161/python_servicios_api_globant/tree/main
