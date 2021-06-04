from fastapi import Request, HTTPException
from typing import Optional
from crud.CRUDNotes import CRUDUser
from models.models import Notes as ModelUser

class UserService():
    async def get_users(request: Request) -> Optional[ModelUser]:
        retrieved_users = await CRUDUser.get_by_email(request)
        if not retrieved_users:
            raise HTTPException(
                status_code=404, 
                detail=f"User with ID {id} not found"
            )
        return retrieved_users

