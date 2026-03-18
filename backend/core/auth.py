from sqlalchemy.orm import Session
from fastapi import HTTPException
from core.models import User

def register_user(username: str, password: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuario registrado", "id": new_user.id}


def login_user(username: str, password: str, db: Session):
    user = db.query(User).filter(
        User.username == username,
        User.password == password
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return {"message": "Login exitoso", "user_id": user.id}
