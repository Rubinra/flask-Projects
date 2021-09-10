from configparser import SafeConfigParser

# create object
config = SafeConfigParser()
directory = 'configuration.ini'
config.read(directory)

# Elastic Search
ELASTIC_HOST = config.get("ELASTICSEARCH", "ELASTICSEARCH_HOST")
