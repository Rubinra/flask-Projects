from flask import request, jsonify, json
from flask.views import MethodView
from applications import es


class Restaurant(MethodView):
    methods = ["GET", "POST"]

    # Add Restaurant(To Add Restaurants)Admin
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        result = es.index(index="restaurant", doc_type="doc", body=json_data)
        return jsonify(result)

    # To fetch all Restaurants
    @staticmethod
    def get():
        query = {"query": {"match_all": {}}, "size": 250}
        results = es.search(index="restaurant", body=query)
        res = results["hits"]["hits"]
        new = []
        for i in range(len(res)):
            new.append(res[i]["_source"])
        return jsonify(new)
