# main.py
import uvicorn
from fastapi import FastAPI
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from models import Notes as ModelUser
from schema import Notes as SchemaUser
from dotenv import load_dotenv

import os
import psycopg2
import dj_database_url


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# DATABASE_URL = os.environ['HEROKU_POSTGRESQL_YELLOW_URL']

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASE_URL = os.environ['DATABASE_URL'].update(db_from_env)
# DATABASES['default'].update(db_from_env)


app = FastAPI()

# app.add_middleware(DBSessionMiddleware, db_url=os.environ["HEROKU_POSTGRESQL_YELLOW_URL"])
# db_url=os.environ.get('HEROKU_POSTGRESQL_YELLOW_URL')
# conn = psycopg2.connect(db_url, sslmode='require')


@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}

# @app.get("/notes/", response_model=SchemaUser)
# def get_user():
#     # db_user = ModelUser(
#     #     text=user.first_name, last_name=user.last_name, age=user.age
#     # )
#     print(db.session.query(ModelUser).count())
#     note = db.session.query(ModelUser).get(8)
#     return note


@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        text=user.text
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
