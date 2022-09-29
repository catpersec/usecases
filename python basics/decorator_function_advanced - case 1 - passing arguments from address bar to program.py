# 1.
#   a| Pass variable from address bar to the program
#   b| Returning passed variable as a string on the website
# 2. Turned on "Debug mode" so website server restarts with every change so
#    client see the changes immediately
#

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function



@app.route('/')
def say_hello():
    return "Hello world"


@app.route('/bye')
@make_bold
@make_underlined
@make_italic

def say_bye():
    return "Bye"

# 1. a|
@app.route('/<name>_<subpage>')
def hello_name(name,subpage):
#   b|
    return f"<h1>Hi master {name} miszczu!</h1>" \
           f"you're on the subpage {subpage}"


# 2.
if __name__ == "__main__":
    app.run(debug=True)