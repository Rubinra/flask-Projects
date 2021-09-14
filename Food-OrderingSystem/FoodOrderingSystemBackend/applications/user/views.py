import json
from flask import jsonify, request
from flask.views import MethodView
from applications import es


class UserRegister(MethodView):
    methods = ["GET", "POST"]

    @staticmethod
    def get():
        api_urls = {
            "1. RegisterUser": "/RegisterNewUser",
            "2. LoginUser": "/LoginUser",
            "3. UpdateUser": "/UpdateUser/<int:id>",
            "4. DeleteUserAccount": "/DeleteUserAccount/<int:id>",
        }
        return api_urls

    # Register User(To Add New User)
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        userId = json_data["id"]
        result = es.index(index="user", doc_type="doc", id=userId, body=json_data)
        return jsonify(result)


class UserLogin(MethodView):
    methods = ["POST"]

    # Login User with Name and Password
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        userName = json_data["Name"]
        password = json_data["Password"]
        query = {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"Name.keyword": userName}},
                        {"term": {"Password.keyword": password}},
                    ]
                }
            }
        }
        results = es.search(index="user", body=query)
        res = results["hits"]["hits"]
        data = {}
        data.update(res[0]["_source"])
        return jsonify(data)

    # # To Delete All Data
    # @staticmethod
    # def delete():
    #     query = {"query": {"match_all": {}}}
    #     result = es.delete_by_query(index="student", body=query)
    #     return " Deleted Successfully" + str(result)


class UserEdit(MethodView):
    methods = ["GET", "POST", "PUT", "DELETE"]

    # # To fetch Data By id
    # @staticmethod
    # def get(id):
    #     query = {"query": {"bool": {"must": [{"match": {"id": id}}]}}}
    #     results = es.search(index="student", body=query)
    #     return results

    # To Update User
    @staticmethod
    def put(id):
        json_data = request.get_json(force=True)
        result = es.index(index="user", doc_type="doc", id=id, body=json_data)
        return jsonify(result)

    # To Delete User Account
    @staticmethod
    def delete(id):
        query = {"query": {"match": {"id": id}}}
        es.delete_by_query(index="user", body=query)
        return "Id " + str(id) + " Deleted Successfully"


class FilterAsSource(MethodView):
    methods = ["GET"]

    # To fetch all Data
    @staticmethod
    def get():
        source = es.search(index="student", filter_path=["hits.hits._source"])
        return source


class FilterAsSourceStudentId(MethodView):
    methods = ["GET"]

    # To fetch all Data
    @staticmethod
    def get():
        StudentId = es.search(index="student", filter_path=["hits.hits._source.id"])
        return StudentId


# To frontend
class GetAllExtractedJson(MethodView):
    methods = ["GET"]

    # To fetch all Data
    @staticmethod
    def get():
        query = {"query": {"match_all": {}}, "size": 250}
        results = es.search(index="student", body=query)
        res = results["hits"]["hits"]
        new = []
        for i in range(len(res)):
            new.append(res[i]["_source"])
        # for j in range(len(new)):
        #     mid = json.dumps(new, indent=4)
        #     mid = json.loads(mid)
        return jsonify(new)


class GetExtractedJsonById(MethodView):
    methods = ["GET", "POST", "PUT", "DELETE"]

    # To fetch Data By id
    @staticmethod
    def get(id):
        query = {"query": {"bool": {"must": [{"term": {"id": id}}]}}}
        results = es.search(index="student", body=query)
        res = results["hits"]["hits"]
        new = {}
        new.update(res[0]["_source"])
        return jsonify(new)
