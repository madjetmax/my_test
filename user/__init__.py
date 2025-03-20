user = "ddd"
status = "user"


class User:
    def __init__(self):
        self.status = "user"

    def add_post(self, text, title):
        print("adding post")


class Admin(User):
    def __init__(self):
        super().__init__(self)

        self.status = "admin"
    
    def get_users(self) -> list[User]:
        print(f"users: {[]}")