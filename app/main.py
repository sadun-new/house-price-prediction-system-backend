#importing required depedencies
from fastapi import FastAPI

# instaling fastapi app
app = FastAPI(
    title="My FastAPI Application",
    description="A simple FastAPI application for demonstration purposes.",
    version="1.0.0"                
)

#endpoints
@app.get("/")
def read_root():
    return {"message": "This is the root of the house prediction price api"}

@app.get("/health")
def read_health():
    return {"status": "ok"} 