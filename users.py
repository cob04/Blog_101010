# users.py

NORMAL = "Normal"
MODERATOR = "Moderator"
ADMIN = "Administtrator"


class User:
    """A user that can make and edit comments."""
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __repr__(self):
        return f"User({self.name}, {self.role})"
