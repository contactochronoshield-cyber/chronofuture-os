from fastapi import FastAPI

app = FastAPI(title="ChronoFuture API")

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
