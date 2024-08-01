from fastapi import FastAPI, HTTPException
from .routers import character_router, login_router, utils_router
from .exceptions import (
    http_exception_handler,
    general_exception_handler,
    validation_exception_handler
)

app = FastAPI()

app.include_router(login_router, prefix="/login", tags=["login"])
app.include_router(character_router, prefix="/character", tags=["character"])
app.include_router(utils_router, prefix="/utils", tags=["utils"])

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)
app.add_exception_handler(ValueError, validation_exception_handler)
