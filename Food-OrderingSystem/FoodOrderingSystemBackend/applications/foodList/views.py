from flask import request, jsonify
from flask.views import MethodView
from applications import es


class Food(MethodView):
    methods = ["GET", "POST", "DELETE"]

    # Add Foods(To Add food items)ADMIN
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        result = es.index(index="foods", doc_type="doc", body=json_data)
        return jsonify(result)

    # To fetch food items based on Restaurants
    @staticmethod
    def get(restaurant):
        query = {"query": {"bool": {"must": [{"match": {"Restuarant": restaurant}}]}}}
        results = es.search(index="foods", body=query)
        res = results["hits"]["hits"]
        new = []
        for i in range(len(res)):
            new.append(res[i]["_source"])
        return jsonify(new)
