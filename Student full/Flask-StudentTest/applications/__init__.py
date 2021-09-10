from elasticsearch import Elasticsearch
from flask import Flask
from flask_cors import CORS

es = Elasticsearch()
app = Flask(__name__)
CORS(app)
from applications.views import *
