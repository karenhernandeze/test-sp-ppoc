from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db.db import notes
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import query, sessionmaker
import os
import databases
import sqlalchemy
from router import notes_router

# CONNECTING TO DB 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
DATABASE_URL= os.environ["DATABASE_URL"]
database = databases.Database(DATABASE_URL)


engine = sqlalchemy.create_engine(
    DATABASE_URL
)
# metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
    try:
        await database.connect()
        print('connected')
    except:
        print("An error occured")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}

app.include_router(router=notes_router.router) 

