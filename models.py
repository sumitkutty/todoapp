
#Here we will be creating sqlite tables

from sqlalchemy import Boolean, Column, Integer, String
from database import Base


# We will create a database, have two separate tables in it. One will be called 'Users' 
# ..which includes ID, EMAIL, FIRST NAME, LAST NAME, HASHED PASSWORD
# The other table will be called TODOS and will contains fields: title, description, priority,  complete

class Todos(Base):
    __tablename__= "todos"
    
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default = False)
    
    
    
    