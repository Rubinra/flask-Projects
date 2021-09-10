from datetime import datetime
from flask import jsonify, request
from flask.views import MethodView

from applications import es


class Home(MethodView):
    methods = ['GET']

    @staticmethod
    def get():
        api_urls = {
            'DataList': '/fetchAllData',
            'GetDataById': '/fetchDataById/<int:id>',
            'AddData': "/addData's",
            'UpdateData': '/updateDataById/<int:id>',
            'DeleteDataById': '/deleteDataById/<int:id>',
            'DeleteAllData': '/deleteAllData',
        }
        return api_urls


class AllStudents(MethodView):
    methods = ['GET', 'POST', 'DELETE']

    # To fetch all Data
    @staticmethod
    def get():
        query = {"query": {"bool": {"must": [{"match_all": {}}], "must_not": [], "should": []}}, "from": 0, "size": 250,
                 "sort": [], "aggs": {}}
        results = es.search(index="student", body=query)
        return results

    # To Add new Data's
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        studentId = json_data['studentId']
        studentName = json_data['studentName']
        studentMarks = json_data['studentMarks']

        body = {
            'studentId': studentId,
            'studentName': studentName,
            'studentMarks': studentMarks,
            'timestamp': datetime.now()
        }

        result = es.index(index='student', doc_type='doc', id=studentId, body=body)

        return jsonify(result)

    # To Delete All Data's
    @staticmethod
    def delete():
        query = {"query": {"match_all": {}}}
        result = es.delete_by_query(index='student', body=query)
        return " Deleted Successfully" + str(result)


class StudentsById(MethodView):
    methods = ['GET', 'POST', 'PUT', 'DELETE']

    # To fetch Data By id
    @staticmethod
    def get(id):
        query = {"query": {"bool": {"must": [{"match": {"studentId": id}}]}}}
        results = es.search(index="student", body=query)
        return results

    # Update Data By Id
    @staticmethod
    def put(id):
        # json_data is a dictionary or a JSON
        json_data = request.get_json(force=True)
        print(json_data)
        studentName = json_data['studentName']
        studentMarks = json_data['studentMarks']

        body = {
            'studentId': id,
            'studentName': studentName,
            'studentMarks': studentMarks,
            'timestamp': datetime.now()
        }
        result = es.index(index='student', doc_type='doc', id=id, body=body)
        return jsonify(result)

    # To Delete Data By id
    @staticmethod
    def delete(id):
        query = {"query": {"match": {"studentId": id}}}
        es.delete_by_query(index='student', body=query)
        return "Id " + str(id) + " Deleted Successfully"

    # # UpdateStudent By Id
    # @staticmethod
    # def put(id):
    #     studentId = id
    #     studentName = request.form['studentName']
    #     studentMarks = request.form['studentMarks']
    #
    #     body = {
    #         "script": {
    #             'studentName': studentName,
    #             'studentMarks': studentMarks,
    #             'timestamp': datetime.now()
    #         },
    #         "query": {"bool": {"must": [{"match": {"studentId": id}}]}}
    #     }
    #
    #     result = es.update_by_query(index='student', doc_type='doc', id=studentId, body=body)
    #     return jsonify(result)


class FilterAsSource(MethodView):
    methods = ['GET']

    # To fetch all Data
    @staticmethod
    def get():
        source = es.search(index="student", filter_path=["hits.hits._source"])
        return source


class FilterAsSourceStudentId(MethodView):
    methods = ['GET']

    # To fetch all Data
    @staticmethod
    def get():
        StudentId = es.search(index="student", filter_path=["hits.hits._source.studentId"])
        return StudentId
