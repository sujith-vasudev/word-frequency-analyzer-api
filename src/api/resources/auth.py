from fastapi import APIRouter, Depends, Body
from starlette import status
from starlette.responses import JSONResponse

from action.auth import UserAction
from api.models.auth import LoginModel, RegisterModel
from db.db_session import get_db_session
from utils.token import create_access_token

auth_router = APIRouter()


@auth_router.post("/login", tags=["Auth"])
def login(payload: LoginModel, session=Depends(get_db_session)):
    user_action = UserAction(session=session)
    user_action.validate_user(username=payload.username, password=payload.password)
    access_token = create_access_token(data={"username": payload.username})
    refresh_token = create_access_token(data={"username": payload.username}, expires_in_minutes=32)
    return JSONResponse(content={
        "status": "success",
        "message": "user logged successfully",
        "result": {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
    }, status_code=status.HTTP_200_OK)


@auth_router.post("/register", tags=["Auth"])
def register_user(payload: RegisterModel = Body(RegisterModel), session=Depends(get_db_session)):
    UserAction(session=session).create_user(username=payload.username, password=payload.password1)
    session.commit()
    return JSONResponse(content={
        "status": "success",
        "message": "user created successfully",
    }, status_code=status.HTTP_201_CREATED)
