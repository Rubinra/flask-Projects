import json
from flask import jsonify, request
from flask.views import MethodView
from applications import es


class Home(MethodView):
    methods = ["GET"]

    @staticmethod
    def get():
        api_urls = {
            "1. DataList": "/fetchAllData",
            "2. GetDataById": "/fetchDataById/<int:id>",
            "3. AddData": "/addData's",
            "4. UpdateData": "/updateDataById/<int:id>",
            "5. DeleteDataById": "/deleteDataById/<int:id>",
            "6. DeleteAllData": "/deleteAllData",
            "7. FilterAsSource": "/fetchAllSourceData",
            "8. FilterAsSourceStudentId": "/fetchAllSourceDataStudentId",
            "9. GetAllExtractedJson": "/fetchAllExtractedJson",
            "GetExtractedJsonById": "/fetchExtractedJsonById/<int:id>",
        }
        return api_urls


class AllStudents(MethodView):
    methods = ["GET", "POST", "DELETE"]

    # To fetch all Data
    @staticmethod
    def get():
        query = {"query": {"bool": {"must": [{"match_all": {}}]}}, "size": 250}
        results = es.search(index="student", body=query)
        return results

    # To Add new Data's
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        studentId = json_data["id"]
        result = es.index(index="student", doc_type="doc", id=studentId, body=json_data)
        return jsonify(result)

    # To Delete All Data's
    @staticmethod
    def delete():
        query = {"query": {"match_all": {}}}
        result = es.delete_by_query(index="student", body=query)
        return " Deleted Successfully" + str(result)


class StudentsById(MethodView):
    methods = ["GET", "POST", "PUT", "DELETE"]

    # To fetch Data By id
    @staticmethod
    def get(id):
        query = {"query": {"bool": {"must": [{"match": {"id": id}}]}}}
        results = es.search(index="student", body=query)
        return results

    # To Update Data By Id
    @staticmethod
    def put(id):
        # json_data is a JSON
        json_data = request.get_json(force=True)
        result = es.index(index="student", doc_type="doc", id=id, body=json_data)
        return jsonify(result)

    # To Delete Data By id
    @staticmethod
    def delete(id):
        query = {"query": {"match": {"id": id}}}
        es.delete_by_query(index="student", body=query)
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
        results = es.search(
            index="student", body={"query": {"match_all": {}}, "size": 250}
        )
        res = json.loads(json.dumps(results))["hits"]["hits"]
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
