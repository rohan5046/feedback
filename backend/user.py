from uuid import uuid4

# TODO: needs to put important creation information in the database
def make_user():
    return User(uuid4())

# TODO: needs to ask database to check this user definitely exists
def load_user(uid):
    return User(uid)

class User:
    def __init__(self, uid):
        self.uid = uid