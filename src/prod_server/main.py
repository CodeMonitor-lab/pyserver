import uvicorn
from fastapi import FastAPI
from render_sdk import Workflows

from prod_server.config import HOST, PORT
from prod_server.routes import user_routes

app = FastAPI()
workflows = Workflows()

app.include_router(user_routes.router)

# render workflows example
@workflows.task()
def calculate_square(a: int) -> int:
    return a * a


@app.get("/")
async def root():
    return {"message": "Server running..."}


def dev():
    uvicorn.run(
        "prod_server.main:app",
        host=HOST,
        port=PORT,
        reload=True,
    )


def prod():
    uvicorn.run(
        "prod_server.main:app",
        host=HOST,
        port=PORT,
        workers=4,
    )


if __name__ == "__main__":
    dev()