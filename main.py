from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return{"success":True,"message":"Hello mcc!"}

@app.get("/about")
def about():
    return {"Name":"Aish","Location":"Mumbai"}
