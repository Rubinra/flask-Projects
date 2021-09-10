from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from database.elasticsearch import *
from applications.urls import *
from applications.user.views import *
