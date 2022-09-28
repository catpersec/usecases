from flask import Flask
import random

print(random.__name__)

app = Flask(__name__)

print(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/s')
def say_goodbye():
    return 'Goodbye'


if __name__ == "__main__":
    app.run()
