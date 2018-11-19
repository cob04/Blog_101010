import datetime


class Comment:
    """docstring for comments"""

    def __init__(self, author, message):
        self.author = author
        self.message = message
        self.timestamp = datetime.datetime.utcnow()
        self.replies = []

    def add_reply(self, comment):
        self.replies.append(comment)
