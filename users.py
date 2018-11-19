# users.py

NORMAL = "Normal"
MODERATOR = "Moderator"
ADMIN = "Administtrator"

LOGGED_IN = "logged in"
LOGGED_OUT = "logged out"

class User:
    """A user that can make and edit comments."""
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.login_status = LOGGED_OUT 

    def __repr__(self):
        return f"User({self.name}, {self.role})"

    def login(self):
        self.login_status = LOGGED_IN
        return "logged in"

    def logout(self):
        if self.login_status == LOGGED_IN:
            self.login_status = LOGGED_OUT
            return "logged out"
        return "already logged out"