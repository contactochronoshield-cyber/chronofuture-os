kkfrom fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔥 PERMITIR TODO (para pruebas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
