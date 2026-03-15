import uvicorn
from fastapi import FastAPI
from prod_server.config import HOST, PORT
from prod_server.routes import user_routes

app = FastAPI()

app.include_router(user_routes.router)


@app.get("/")
async def root():
    return {"message": "Server running..."}


def dev():
    uvicorn.run(
        "prod_server.main:app",
        host=HOST,
        port=PORT,
        reload=True,
        reload_dirs=["src"],
    )


def prod():
    uvicorn.run(
        "prod_server.main:app",
        host=HOST,
        port=PORT,
        reload=False,
        workers=4,
    )