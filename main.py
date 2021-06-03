# main.py
from fastapi import FastAPI
from typing import List
# import databases
# import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
import os
from fastapi_sqlalchemy import DBSessionMiddleware
# from fastapi_sqlalchemy import db
from models import Notes as ModelUser
from schema import Notes as SchemaUser
from dotenv import load_dotenv

# DATABASE_URL = "postgresql://postgres:12345678@database-2.ckgekixw3q0p.us-east-1.rds.amazonaws.com/postgres"
# database = databases.Database(DATABASE_URL)
# # metadata = sqlalchemy.MetaData()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}