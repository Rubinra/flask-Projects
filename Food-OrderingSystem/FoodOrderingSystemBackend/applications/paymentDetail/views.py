from flask import jsonify, request
from flask.views import MethodView
from applications import es


# class Payment(MethodView):
#     methods = ["POST", "DELETE"]

# Add to payment-details
# @staticmethod
# def post():
#     query1 = {"query": {"match_all": {}}, "size": 250}
#     results1 = es.search(index="food-cart", body=query1)
#     res1 = results1["hits"]["hits"]
#     cart = []
#     for i in range(len(res1)):
#         cart.append(res1[i]["_source"])
#         totalPrice = cart[i]["Total Price"]
#     deliveryCharge = 40
#     tax = 10
#     amount = totalPrice + deliveryCharge + tax
#
#     query2 = {"query": {"match_all": {}}, "size": 250}
#     results2 = es.search(index="user", body=query2)
#     res2 = results2["hits"]["hits"]
#     user = []
#     for i in range(len(res2)):
#         user.append(res2[i]["_source"])
#         address = user[i]["Address"]
#     paymentMethod = "COD"
#     json_data = {}
#     json_data.update({"Cart": cart})
#     json_data.update({"Address": address})
#     json_data.update({"Amount to pay": amount})
#     json_data.update({"Payment Method": paymentMethod})
#     result = es.index(index="payment-details", doc_type="doc", body=json_data)
#     return jsonify(result)


class Payment(MethodView):
    methods = ["GET", "POST", "DELETE"]

    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        userId = json_data["Uid"]

        query1 = {"query": {"bool": {"must": [{"term": {"Uid": userId}}]}}}
        results1 = es.search(index="food-cart", body=query1)
        res1 = results1["hits"]["hits"]
        cart = []
        totalPrice = 0
        for i in range(len(res1)):
            cart.append(res1[i]["_source"])
            totalPrice = totalPrice + cart[i]["Total Price"]
        deliveryCharge = 40
        tax = 10
        amount = totalPrice + deliveryCharge + tax

        query2 = {"query": {"bool": {"must": [{"term": {"id": userId}}]}}}
        results2 = es.search(index="user", body=query2)
        res2 = results2["hits"]["hits"]
        user = []
        for i in range(len(res2)):
            user.append(res2[i]["_source"])
            address = user[i]["Address"]

        paymentMethod = "COD"
        json_data = {}
        json_data.update({"Cart": cart})
        json_data.update({"Address": address})
        json_data.update({"Amount to pay": amount})
        json_data.update({"Payment Method": paymentMethod})
        result = es.index(index="payment-details", doc_type="doc", body=json_data)
        return jsonify(result)

    # To Delete All Data After delivery
    @staticmethod
    def delete(id):
        query1 = {"query": {"bool": {"must": [{"term": {"Uid": id}}]}}}
        query2 = {"query": {"bool": {"must": [{"term": {"Cart.Uid": id}}]}}}
        result1 = es.delete_by_query(index="food-cart", body=query1)
        result2 = es.delete_by_query(index="payment-details", body=query2)

        return "Deleted Successfully food-cart\n\n" + str(result1) + " \n\nDeleted Successfully payment-details \n\n" + str(result2)
