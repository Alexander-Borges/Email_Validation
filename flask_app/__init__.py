from flask import Flask
app = Flask(__name__)
app.secret_key = "Super_Secret"

from flask_app.controllers import users 

