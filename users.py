# users.py

from comments import Comment


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
        self.comments = []

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

    def create_comment(self, message):
        """Create a comment by this author."""
        new_comment = Comment(message, self)
        self.comments.append(new_comment)
        return new_comment

    def view_comments(self):
        """Show all the comments a user has."""
        return self.comments

    def edit_comment(self, comment, message):
        """Edit a users Comments."""
        if comment in self.comments:
            comment.message = message
        return comment


class Moderator(User):
    """User of the role moderator."""
    pass
