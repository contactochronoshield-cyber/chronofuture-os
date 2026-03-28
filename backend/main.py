from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database.db import Base, engine, SessionLocal
from core.models import User

app = FastAPI()

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

# CORS (permite conexión desde frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión a DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas básicas
@app.get("/")
def root():
    return {"message": "ChronoFuture está ONLINE 🚀"}

@app.get("/system")
def system():
    return {
        "name": "ChronoFuture OS",
        "status": "active",
        "version": "3.2"
    }

# Registro
@app.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Usuario creado"}

# Login
@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user or user.password != password:
        return {"error": "Credenciales incorrectas"}

    return {"message": "Bienvenido " + user.username}
