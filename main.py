# main.py
from fastapi import FastAPI
from typing import List
# import databases
# import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

# DATABASE_URL = "postgresql://postgres:12345678@database-2.ckgekixw3q0p.us-east-1.rds.amazonaws.com/postgres"
# database = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}