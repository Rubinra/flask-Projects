from elasticsearch import Elasticsearch
from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

es = Elasticsearch([app.config["ELASTICHOST"]])

from applications.views import *
