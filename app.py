# app.py
from flask import Flask, render_template
from controller import UserController

app = Flask(__name__)
user_controller = UserController()

@app.route('/')
def index():
    users = user_controller.get_users()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run()
