from fastapi import APIRouter
from prod_server.schemas.user_schema import UserCreate
from prod_server.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

service = UserService()


# create user
@router.post("/")
def create_user(user: UserCreate):
    user_info = user.model_dump()   # Pydantic v2 method
    print(f"Received user data: {user_info}")
    return service.create_user(user_info)


# get all users
@router.get("/")
def get_all_users():
    return service.get_all_users()


# get user by id
@router.get("/{user_id}")
def get_user(user_id: str):
    return service.get_user(user_id)

# delete user by id
@router.delete("/{user_id}")
def delete_user(user_id: str):
    return service.delete_user(user_id)