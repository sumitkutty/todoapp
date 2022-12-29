
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--database_path", help = "Database Path", nargs ='?', default = "DB/todos.db")
args = parser.parse_args()



database_path = args.database_path

dirs = '/'.join(database_path.split('/')[:-1])

os.makedirs(dirs, exist_ok = True)

# URL to the database file
SQLALCHEMY_DATABASE_URL =  f"sqlite:///./{database_path}"


# create a sqlalchemy engine.Engine is the route through which we communicate with DB
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args= {"check_same_thread": False})

#create new database session
session_local = sessionmaker(autocommit = False, autoflush=False, bind=engine)

#Create base. base will allow to create each DB model. 
Base = declarative_base()

#Create the database with todos table in current folder
#models.Base.metadata.create_all(bind=engine)
#running till here will create the .db file