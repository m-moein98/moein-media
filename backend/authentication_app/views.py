import datetime

from bson.objectid import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from settings import (ACCESS_TOKEN_EXPIRE_MINUTES, token_collection,
                     user_collection)

from authentication_app.auth import (authenticate_user, create_access_token,
                                     get_password_hash, get_user, oauth2_scheme)

from .models import UpdateUser, User
from .serializers import user_serilaizer

api_router = APIRouter()


@api_router.post("/token")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    access_token_expires = datetime.timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, userId=user['_id'], expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@api_router.post("/create-user")
async def create_user(username: str, password: str, email: str):
    user = User(
        username=username, password=get_password_hash(password), email=email)
    _id = user_collection.insert_one(dict(user))
    instance = user_collection.find_one({"_id": _id.inserted_id})
    return user_serilaizer(instance)


@api_router.get("/get-user")
async def get_user_data(token: str = Depends(oauth2_scheme)):
    token = token_collection.find_one({"token": token})
    user = user_collection.find_one({"_id": ObjectId(token["userId"])})
    return user_serilaizer(user)


@api_router.put("/update-user")
async def update_user(user: UpdateUser, token: str = Depends(oauth2_scheme)):
    token_instance = token_collection.find_one({"token": token})
    if not token_instance:
        raise HTTPException(
            status_code=400, detail="Incorrect token")
    if not get_user(token):
        raise HTTPException(
            status_code=400, detail="Incorrect user")

    user_collection.find_one_and_update(
        {"_id": ObjectId(token_instance["userId"])},
        {"$set": user.dict()}
    )
    user = user_collection.find_one({"_id": ObjectId(token_instance["userId"])})
    return user_serilaizer(user)
