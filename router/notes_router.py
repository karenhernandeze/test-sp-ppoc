from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from models.models import Notes as ModelUser
from service.service import UserService 

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description" : "Not found"}}
)


@router.get("/notes/", status_code=status.HTTP_200_OK, response_description="List all reservations by User", response_model=List[ModelUser])
async def read_notes(request: Request):
    # return "HELLOE WORDL"
    query = await UserService.get_users(request)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": query})

# @app.post("/user/", response_model=SchemaUser)
# def create_user(user: SchemaUser):
#     db_user = ModelUser(
#         text=user.text
#     )
#     db.session.add(db_user)
#     db.session.commit()
#     return db_user

