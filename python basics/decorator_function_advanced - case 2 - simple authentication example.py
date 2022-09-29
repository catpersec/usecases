# Advanced Decorators with *args and **kwargs
# Case with simple authentication example.
# Tags: OOP, Advanced Function Decorators, *args, **kwargs
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
        self.password = "Test"

    def authenticate_user(self, typed_password):
        if typed_password == self.password:
            self.is_logged_in = True


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            print()
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("tomek")
password_to_check = input("Password: ")
new_user.authenticate_user(password_to_check)
create_blog_post(new_user)