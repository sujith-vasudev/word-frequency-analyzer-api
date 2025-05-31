import requests
from bs4 import BeautifulSoup
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from action.analyze import analyze_url
from action.auth import UserAction
from api.auth.authentication import token_auth_scheme
from api.models.analyze import AnalyzeRequest
from db.db_session import get_db_session
from utils.token import get_user

analyze_router = APIRouter()


@analyze_router.post("/analyze", tags=["Analyze"])
async def analyze(request: AnalyzeRequest, current_user_info=Depends(get_user), session=Depends(get_db_session)):
    user_obj = UserAction(session=session).validate_username(username=current_user_info['username'])
    top_words = analyze_url(session=session, url=request.url, current_user=user_obj)
    session.commit()
    return {"topWords": top_words}
