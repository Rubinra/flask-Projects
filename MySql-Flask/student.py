from flask import Flask, jsonify, request, make_response
from flask_marshmallow import Marshmallow, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Global12$@localhost/students'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


# SQLAlchemy Model
class StudentMsql(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    marks = db.Column(db.Integer)


# Marshmallow Schemas
class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = StudentMsql

    id = ma.auto_field()
    name = ma.auto_field()
    marks = ma.auto_field()


# class StudentSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = StudentMsql
#         load_instance = True


db.create_all()
Student_schema = StudentSchema(many=True)


@app.route('/', methods=['GET'])
def test_Api():
    return {"status": "Success"}


@app.route('/get-student', methods=['GET'])
def getStudent():
    all_stud = StudentMsql.query.all()
    return jsonify(Student_schema.dump(all_stud))


# To fetch Students By id
@app.route('/get-student/<int:id>/', methods=['GET'])
def getStudentById(id):
    stud = StudentMsql.query.get(id)
    Student_schema = StudentSchema()
    return Student_schema.jsonify(stud)


# post a json
@app.route('/add-student', methods=['POST'])
def createStudent():
    json_data = request.get_json(force=True)
    id = json_data['id']
    name = json_data['name']
    marks = json_data['marks']
    stud = StudentMsql(id=id, name=name, marks=marks)
    db.session.add(stud)
    db.session.commit()
    return json_data


# post a list of data
@app.route('/add-student-list', methods=['POST'])
def createStudentList():
    json_data = request.get_json(force=True)
    lists = json_data["student"]
    for element in range(len(lists)):
        id = lists[element]['id']
        name = lists[element]['name']
        marks = lists[element]['marks']
        stud = StudentMsql(id=id, name=name, marks=marks)
        db.session.add(stud)
        db.session.commit()

    return json_data


# To Update Student By Id
@app.route('/update-StudentById/<int:id>', methods=['PUT'])
def update_data(id):
    name = request.json.get('name')
    marks = request.json.get('marks')
    stud = StudentMsql.query.get(id)
    Student_schema = StudentSchema()
    stud.name = name
    stud.marks = marks
    db.session.add(stud)
    db.session.commit()
    return Student_schema.jsonify(stud)


# To Delete Student By Id
@app.route('/delete-StudentById/<int:id>', methods=['DELETE'])
def delete_data(id):
    stud = StudentMsql.query.get(id)
    Student_schema = StudentSchema()
    db.session.delete(stud)
    db.session.commit()
    return Student_schema.jsonify(stud)


# To Delete All Student
@app.route('/delete-AllStudent', methods=['DELETE'])
def delete_AllData():
    StudentMsql.query.delete()
    db.session.commit()
    return "Deleted all Successfully"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
