from elasticsearch import Elasticsearch
from applications import app

app.config.from_object("config")
es = Elasticsearch([app.config["ELASTIC_HOST"]])
