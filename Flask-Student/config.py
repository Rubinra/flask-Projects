from configparser import SafeConfigParser

# create object
config = SafeConfigParser()
config.read('E:/python/Flask_Projects/flask-Projects/Flask-Student/configuration.ini')

# Elastic Search
ELASTICHOST = config.get("ELASTICSEARCH", "ELASTIC_HOST")

