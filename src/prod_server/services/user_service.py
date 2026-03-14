from bson import ObjectId
from prod_server.db.connection import db


class UserService:

    # create user
    def create_user(self, user_data):
        result = db.users.insert_one(user_data)
        return {"id": str(result.inserted_id)}

    # get user by id
    def get_user(self, user_id):
        user = db.users.find_one({"_id": ObjectId(user_id)})

        if user:
            return {
                "id": str(user["_id"]),
                "name": user.get("name"),
                "email": user.get("email"),
            }

        return {"error": "User not found"}

    # get all users
    def get_all_users(self):
        users = db.users.find()

        return [
            {
                "id": str(user["_id"]),
                "name": user.get("name"),
                "email": user.get("email"),
            }
            for user in users
        ]

    # update user
    def update_user(self, user_id, update_data):
        result = db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )

        if result.modified_count == 1:
            return {"message": "User updated successfully"}

        return {"error": "User not found"}

    # delete user
    def delete_user(self, user_id):
        result = db.users.delete_one({"_id": ObjectId(user_id)})

        if result.deleted_count == 1:
            return {"message": "User deleted successfully"}

        return {"error": "User not found"}