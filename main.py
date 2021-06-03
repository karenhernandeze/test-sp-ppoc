# main.py
from fastapi import FastAPI
from typing import List
# import databases
# import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
import os
import psycopg2
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from models import Notes as ModelUser
from schema import Notes as SchemaUser
# from dotenv import load_dotenv

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

# app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
db_url=os.environ.get('HEROKU_POSTGRESQL_YELLOW_URL')
conn = psycopg2.connect(db_url, sslmode='require')


@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}

# @app.get("/notes/", response_model=List[SchemaUser])
# def create_user():
#     # db_user = ModelUser(
#     #     text=user.first_name, last_name=user.last_name, age=user.age
#     # )
#     note = db.session.query(ModelUser)
#     return note

@app.get("/notes/", response_model=SchemaUser)
def get_user():
    # db_user = ModelUser(
    #     text=user.first_name, last_name=user.last_name, age=user.age
    # )
    print(db.session.query(ModelUser).count())
    note = db.session.query(ModelUser).get(8)
    return note


@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        text=user.text
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user
