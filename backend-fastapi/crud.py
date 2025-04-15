from backend.models import Todo
from backend.schemas import TodoCreate, TodoUpdate
from sqlalchemy.orm import Session

def get_all_todos(db: Session):
    return db.query(Todo).all()

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(title=todo.title, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db_todo.title = todo.title
        db_todo.completed = todo.completed
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo

def filter_todos_by_status(db: Session, status: str):
    if status.lower() == "completed":
        return db.query(Todo).filter(Todo.completed == True).all()
    elif status.lower() == "pending":
        return db.query(Todo).filter(Todo.completed == False).all()
    return get_all_todos(db)