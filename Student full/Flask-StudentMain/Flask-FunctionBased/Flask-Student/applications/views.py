from datetime import datetime
from flask import jsonify, request

from applications import app, es


@app.route('/', methods=['GET'])
def urls():
    api_urls = {
        'StudentList': '/fetchAllStudents',
        'GetStudentById': '/fetchStudentById/<int:id>',
        'AddStudents': '/addStudents',
        'UpdateStudent': '/updateStudentById/<int:id>',
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
@app.route('/fetchStudentById/<int:id>', methods=['GET'])
def getStudentById(id):
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


# To Update Student By Id
@app.route('/updateStudentById/<int:id>', methods=['PUT'])
def update_data(id):
    studentId = id
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


# To Delete Student By Id
@app.route('/deleteStudentById/<int:id>', methods=['POST'])
def delete_data(id):
    query = {"query": {"match": {"studentId": id}}}
    es.delete_by_query(index='student', body=query)
    return "Id " + id + " Deleted Successfully"


# To Delete All Students
@app.route('/deleteAllStudents', methods=['POST'])
def delete_AllData():
    query = {"query": {"match_all": {}}}
    result = es.delete_by_query(index='student', body=query)
    return result
