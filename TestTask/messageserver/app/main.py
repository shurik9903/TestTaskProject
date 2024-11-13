
from fastapi import FastAPI
import uvicorn
from web.api.description import api_description, api_tags
from web.api import messages_router

from database.mongo_db import client

app = FastAPI(
    title="Messenger Service",
    description=api_description,
    version="0.1.0",
    openapi_tags=api_tags
)

app.include_router(messages_router.router)

if __name__ == "__main__":
    uvicorn.run(app)