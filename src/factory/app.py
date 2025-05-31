
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from api.resources import auth_router, analyze_router
from db.sqlalchemy import start_mappers
from exceptions import ValidationError, AccessExpired

app = FastAPI(title="Demo")


@app.on_event("startup")
def build_db_mappers():
    start_mappers()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(analyze_router)


@app.exception_handler(AccessExpired)
@app.exception_handler(ValidationError)
async def custom_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=exc.status_code,
                        content={"error_code": exc.ERROR_CODE, "message": exc.args[0]})
