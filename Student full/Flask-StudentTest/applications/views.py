from datetime import datetime
from flask import jsonify, request

from applications import app, es
from applications.logic import queryJson
from applications.model import Student


@app.route('/', methods=['GET'])
def urls():
    api_urls = {
        'StudentList': '/fetchAllStudents',
        'GetStudentById': '/fetchStudentById/<int:id>',
        'AddStudents': '/addStudents',
        'UpdateStudent': '/updateStudent/<int:id>/',
        'DeleteStudentById': '/deleteStudentById/<int:id>',
        'DeleteAllStudents': '/deleteAllStudents',
    }
    return api_urls


# To fetch all Students
@app.route('/fetchAllStudents', methods=['GET'])
def getAllStudent():
    query = {"query": {"match_all": {}}}
    results = es.search(index="student", body=query)
    return results


# To fetch Students By id
@app.route('/fetchStudentById/<int:id>/', methods=['GET'])
def studentById(id):
    query = {"query": {"bool": {"must": [{"match": {"studentId": id}}]}}}
    results = es.search(index="student", body=query)
    return results


# To Add new Students
@app.route('/addStudents', methods=['POST'])
def insert_data():
    studentId = request.form['studentId']
    studentName = request.form['studentName']
    studentMarks = request.form['studentMarks']

    body = {
        'studentId': studentId,
        'studentName': studentName,
        'studentMarks': studentMarks,
        'timestamp': datetime.now()
    }

    result = es.index(index='student', doc_type='doc', id=studentId, body=body)
    return jsonify(result)


# # To Update Student By Id
# @app.route('/updateStudentById/<int:id>/', methods=['PUT'])
# def update_data():
#
#     studentId = request.form['studentId']
#     studentName = request.form['studentName']
#     studentMarks = request.form['studentMarks']
#
#     body = {
#         'studentId': studentId,
#         'studentName': studentName,
#         'studentMarks': studentMarks,
#         'timestamp': datetime.now()
#     }
#
#     result = es.update_by_query(index='student', doc_type='doc', id=studentId, body=body)
#
#     return jsonify(result)


# To Delete Students
@app.route('/deleteStudentById/<int:id>/', methods=['POST'])
def delete_data(id):
    query = {"query": {"match": {"studentId": id}}}
    result = es.delete_by_query(index='student', body=query)
    return result


# To Delete All Students
@app.route('/deleteAllStudents', methods=['POST'])
def delete_AllData():
    query = {"query": {"match_all": {}}}
    result = es.delete_by_query(index='student', body=query)
    return result


data = {"Name": "sabu", "Age": 25, "address": "padivattom"}


@app.route('/post', methods=['GET'])
def send_data_to_es():
    # es=Elasticsearch(['localhost:9200'])
    res = es.index(index='student', doc_type='doc', body=data)
    return res


# student = Student()
#
#
# #  # Call method to store data in ES
# # send_data_to_es(data)
# @app.route('/post1', methods=['POST'])
# def send_data_to_es1(student=Student()):
#     # es=Elasticsearch(['localhost:9200'])
#     body = {
#         'studentId': student.stud_id,
#         'studentName': student.name,
#         'studentMarks': student.marks,
#         'timestamp': datetime.now()
#     }
#
#     res = es.index(index='student', doc_type='doc', body=body)
#     return res


@app.route('/VectorQuery', methods=['GET'])
def VectorQuery():
    return queryJson()


# To Add JSON
@app.route('/addVectorQuery')
def addVectorQuery():
    query_Json = queryJson()
    for i in range(len(query_Json)):
        body = (query_Json[i])
        es.index(index='query', doc_type='_doc', body=body)
    return "Successfully Hit JSON"


# To Get JSON
@app.route('/getVectorQuery', methods=['GET'])
def getVectorQuery():
    query = {"query": {"bool": {"must": [{"match_all": {}}], "must_not": [], "should": []}}, "from": 0, "size": 250, "sort": [], "aggs": {}}
    results = es.search(index="query", body=query)
    return results
