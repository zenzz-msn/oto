from flask import Flask
from app.controller.library import library
from app.controller.store import store

app = Flask(__name__)

app.register_blueprint(library)
app.register_blueprint(store)