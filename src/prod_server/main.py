from fastapi import FastAPI
import uvicorn
# imported routes
from prod_server.routes import user_routes

app = FastAPI()
app.include_router(user_routes.router)


@app.get("/")
async def root():
    return {"message": "Server running..."}

def dev():
    uvicorn.run(
        "prod_server.main:app",
        host="127.0.0.1",
        port=8000,
        reload= True,
        app_dir="src",
    )

