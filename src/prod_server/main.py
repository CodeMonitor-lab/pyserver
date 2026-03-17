import uvicorn
import os
from fastapi import FastAPI
from render_sdk import Workflows

from prod_server.routes import user_routes

app = FastAPI()
workflows = Workflows()

app.include_router(user_routes.router)

@workflows.task()
def calculate_square(a: int) -> int:
    return a * a


@app.get("/")
async def root():
    return {"message": "Server running..."}


def dev():
    uvicorn.run(
        "prod_server.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


def prod():
    uvicorn.run(
        "prod_server.main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        workers=1,
    )