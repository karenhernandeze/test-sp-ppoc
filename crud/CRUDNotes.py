# from main import DATABASE_URL
from typing import Optional
from fastapi import Request
from fastapi.encoders import jsonable_encoder
# from models import user_model
from models.models import Notes as ModelUser
from db.db import notes
import databases
from core.settings import settings

database = databases.Database(settings.DATABASE_URL)

class CRUDUser():
    async def get_by_email(request: Request) -> Optional[ModelUser]:
        query = notes.select()
        await database.connect()
        notes_ret = await database.fetch_all(query)

        serialized_hours = jsonable_encoder(notes_ret)
        # if (user := await request.app.mongodb[settings.MONGODB_COLLECTION].find_one({"email": user_in['email']})) is not None:
        #     return user
        # else: return None
        print(serialized_hours)
        return serialized_hours