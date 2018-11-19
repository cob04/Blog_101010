# users.py

from comments import Comment


NORMAL = "Normal"
MODERATOR = "Moderator"
ADMIN = "Administtrator"

LOGGED_IN = "logged in"
LOGGED_OUT = "logged out"


class User:
    """A user that can make and edit comments."""
    def __init__(self, username, password, role=None):
        self.username = username
        self._password = password
        self.role = role or NORMAL
        self.login_status = LOGGED_OUT
        self.comments = []

    def __repr__(self):
        return f"User({self.username}, {self.role})"

    def __str__(self):
        return f"{self.username}"

    def login(self, username, password):
        if username == self.username and password == self._password:
            self.login_status = LOGGED_IN
            return self
        else:
            return False

    def logout(self):
        if self.login_status == LOGGED_IN:
            self.login_status = LOGGED_OUT
            return "logged out"
        return "already logged out"

    def create_comment(self, message):
        """Create a comment by this author."""
        new_comment = Comment(self, message)
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
    def delete_comment(self, comment):
        author = comment.author
        comment_index = author.view_comments().index(comment)
        author.view_comments().pop(comment_index)
        return "comment deleted"
