# controller.py
from model import UserModel

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def get_users(self):
        users = self.user_model.get_users()
        return users
