from flask import Flask

app = Flask(__name__)

from database.elasticsearch import *
from applications.views import *
from applications.urls import *
