from flask import jsonify, request
from flask.views import MethodView
from applications import es


class Cart(MethodView):
    methods = ["GET", "POST", "DELETE"]

    # To fetch all Data
    # @staticmethod
    # def get():
    #     query = {"query": {"match_all": {}}, "size": 250}
    #     results = es.search(index="foods", body=query)
    #     res = results["hits"]["hits"]
    #     food = []
    #     for i in range(len(res)):
    #         food.append(res[i]["_source"])
    #     return jsonify(food)

    # Add to Cart(To Add all food items to cart )
    # @staticmethod
    # def post():
    #     query = {"query": {"match_all": {}}, "size": 250}
    #     results = es.search(index="foods", body=query)
    #     res = results["hits"]["hits"]
    #     food = []
    #     for i in range(len(res)):
    #         food.append(res[i]["_source"])
    #
    #     # food = Cart.get()
    #     itemNum = len(food)
    #     totalPrice = 0
    #     for item in range(0, len(food)):
    #         del food[item]["Type"]
    #         totalPrice = totalPrice + food[item]["Unit Price"] * food[item]["Count"]
    #     json_data = {}
    #     json_data.update({"Food": food})
    #     json_data.update({"No.of Items": itemNum})
    #     json_data.update({"Total Price": totalPrice})
    #     result = es.index(index="food-cart", doc_type="doc", body=json_data)
    #     return jsonify(result)

    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        foodName = json_data["Name"]
        count = json_data["Count"]
        userId = json_data["Uid"]
        query = {"query": {"bool": {"must": [{"match": {"Name": foodName}}]}}}
        results = es.search(index="foods", body=query)
        res = results["hits"]["hits"]
        food = {}
        food.update(res[0]["_source"])
        food.update({"Count": count})
        itemNum = count
        totalPrice = food["Unit Price"] * food["Count"]
        json_data = {}
        json_data.update({"Food": food})
        json_data.update({"No.of Items": itemNum})
        json_data.update({"Total Price": totalPrice})
        json_data.update({"Uid": userId})
        result = es.index(index="food-cart", doc_type="doc", body=json_data)
        return jsonify(result)
