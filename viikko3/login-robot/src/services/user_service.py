from entities.user import User

import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if len(username) < 3:
            raise UserInputError("Username length should be 3 at minimum")
        if bool(re.match("^[a-z]+$", username)) == False:
            raise UserInputError("Username should only contains letters")
        
        if len(password) < 8:
            raise UserInputError("Password length should be 8 at minimum")
        if bool(re.match("[a-z]+?[0-9]+", password)) == False:
            raise UserInputError("Password should contain numbers and letters")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
