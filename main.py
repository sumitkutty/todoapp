# To-DO
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, session_local
import uvicorn
from sqlalchemy.orm import Session
from pydantic import BaseModel , Field


app = FastAPI()

#Create the database with todos table in current folder
models.Base.metadata.create_all(bind=engine)
#running till here will create the .db file



#Retrieve the database
# Now we have to be able to talk to the database (todos.db) created 
def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()

# Class to represent set of fields         
class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="Enter from 1 to 5")
    complete: bool
    
#The parameter in the function below means: take a db of type Session which should run when 'get_db' has run
@app.get("/")
async def read_all(db:Session = Depends(get_db)):
    #return all tables from models.Todos table.
    return "Run is Successful", db.query(models.Todos).all()
    #now, we can execute this and check the tables in localhost/8000


#API to return a record by passing todo_id
@app.get("/todo/{todo_id}")
async def get_todo(todo_id:int, db:Session = Depends(get_db)):
    todo_model = db.query(models.Todos) \
                   .filter(models.Todos.id == todo_id) \
                   .first()
    if todo_model is not None:
        return todo_model
    else:
        raise http_exception()
    
# add a record to the database
@app.post("/todo/add_todo")    
async def add_todo(todo: Todo, db:Session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    
    # Add the records to the database
    db.add(todo_model)
    # Push the records to the database
    db.commit()
    
    return {"Status" : 201,
            'transaction': 'Successful'}
    
    
# Change a record in the database    
@app.put("/todo/{todo_id}")
async def modify_todo(todo_id:int, todo: Todo, db:Session = Depends(get_db)):
    todo_model = db.query(models.Todos) \
                   .filter(models.Todos.id == todo_id) \
                   .first()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    # Add the records to the database
    db.add(todo_model)
    # Push the records to the database
    db.commit()
    return {"Status" : 201,
            'transaction': 'Successful'}
    
#delete a record in the database
@app.delete("/todo/{todo_id}")    
async def delete_todo(todo_id, db:Session = Depends(get_db)):
    todo_model = db.query(models.Todos) \
                .filter(models.Todos.id == todo_id) \
                .first()
                
    if not todo_model:
        raise http_exception()
                
    db.delete(todo_model)
    db.commit()
    return {"Status" : 201,
            'transaction': 'Successful'}, read_all()
    
# Creating a new http exception
def http_exception():
    return HTTPException(status_code = 404, detail = 'Item not Found')


# Learn Authentication from udemy after this: JWT: JSON Web Token

if __name__ == "__main__":
    print('Run is Successful')
    uvicorn.run(app="main:app", reload=True, host="0.0.0.0", port=8000)