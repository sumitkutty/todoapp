# FastAPI-SQLite App
#### This is a project to create and operate a SQLite database through an API.

## Database:
* Database is created using a serverless, cross-platform, in-process library called SQLite. 
* SQLite is a database engine that is used in an embedded context while requiring not additional database server.
* SQLAlchemy, a SQL toolkit for Python is used to create the SQLite engine.


## API:
* FastAPI is used to create an interface between the end-user and the database engine. 
* Functions in the API include creating, adding, modifying and deleting records in the database.

## Tools
* Python3
* Docker 
* FastAPI
* SQLite3



## Usage:
 ### **Local**

```shell
> git clone git@github.com:sumitkutty/todoapp.git

> cd todoapp

# Install Dependancies
> pip install -r requirements.txt

#creates the database
> python3 database.py -d DB/database_name.db

> python3 main.py 
# -> localhost:8000
```

### **Using Docker**
```shell
> git clone git@github.com:sumitkutty/todoapp.git

> cd todoapp

> docker build -t username/image_name:tag

> docker run -p 8000:8080 username/image_name:tag
# -> localhost:8000
```