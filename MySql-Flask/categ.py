from flask import Flask, jsonify, request, make_response
from flask_marshmallow import Marshmallow, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Global12$@localhost/categories'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


# SQLAlchemy Model
class Categories(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    param = db.Column(db.String(255))
    types = db.Column(db.String(255))
    displayName = db.Column(db.String(255))


# Marshmallow Schemas
class CategoriesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categories

    id = ma.auto_field()
    param = ma.auto_field()
    types = ma.auto_field()
    displayName = ma.auto_field()


# class StudentSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = StudentMsql
#         load_instance = True


db.create_all()
Categories_schema = CategoriesSchema(many=True)


@app.route('/', methods=['GET'])
def test_Api():
    return {"status": "Success"}


@app.route('/get-Categories', methods=['GET'])
def getCategories():
    all_categ = Categories.query.all()
    return jsonify(Categories_schema.dump(all_categ))


# post a json
@app.route('/add-Categories', methods=['POST'])
def createCategories():
    json_data = request.get_json(force=True)
    id = json_data['id']
    param = json_data['param']
    types = json_data['type']
    displayName = json_data['displayName']
    categ = Categories(id=id, param=param, types=types, displayName=displayName)
    db.session.add(categ)
    db.session.commit()
    return json_data


# post a list of data
@app.route('/add-Categories-list', methods=['POST'])
def createCategoriesList():
    json_data = request.get_json(force=True)
    lists = json_data["data"]
    for element in range(len(lists)):
        param = lists[element]['param']
        types = lists[element]['types']
        dispalayName = lists[element]['displayName']
        categ = Categories(param=param, types=types, displayName=dispalayName)
        db.session.add(categ)
        db.session.commit()

    return json_data


if __name__ == "__main__":
    app.run(debug=True, port=5002)
