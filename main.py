from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import engine, Base, get_db
import backend.models as models, backend.schemas as schemas, backend.crud as crud

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Create a new todo
@app.post("/todos")
def create(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

# Read all todos
@app.get("/todos")
def read_all(db: Session = Depends(get_db)):
    return crud.get_all_todos(db)

# Read a single todo by ID
@app.get("/todos/{todo_id}")
def read_one(todo_id: int, db: Session = Depends(get_db)):
    return crud.get_todo(db, todo_id)

# Update a todo
@app.put("/todos/{todo_id}")
def update(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    return crud.update_todo(db, todo_id, todo)

# Delete a todo
@app.delete("/todos/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    return crud.delete_todo(db, todo_id)

# Filter todos by status (completed/pending)
@app.get("/todos/filter/{status}")
def filter(status: str, db: Session = Depends(get_db)):
    return crud.filter_todos_by_status(db, status)
