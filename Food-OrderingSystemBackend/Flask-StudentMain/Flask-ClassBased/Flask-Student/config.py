from configparser import SafeConfigParser

# create object
config = SafeConfigParser()
directory = 'C:/Users/Shon/Desktop/Shon/PYTHON/PythonLanguage/Pycharm/FLASK/Flask-First-Programs/Flask-Student/Flask-StudentMain/Flask-ClassBased/Flask-Student/configuration.ini'
config.read(directory)

# Elastic Search
ELASTICHOST = config.get("ELASTICSEARCH", "ELASTIC_HOST")
