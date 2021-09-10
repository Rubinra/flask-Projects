from applications import app
from .views import *

app.add_url_rule('/', view_func=Home.as_view(''))
app.add_url_rule('/fetchAllData', view_func=AllStudents.as_view('fetchAllData'))
app.add_url_rule('/fetchDataById/<int:id>', view_func=StudentsById.as_view('fetchDataById'))
app.add_url_rule("/addData's", view_func=AllStudents.as_view("addData's"))
app.add_url_rule("/updateDataById/<int:id>", view_func=StudentsById.as_view('updateDataById'))
app.add_url_rule("/deleteDataById/<int:id>", view_func=StudentsById.as_view('deleteDataById'))
app.add_url_rule("/deleteAllData", view_func=AllStudents.as_view('deleteAllData'))

app.add_url_rule('/fetchAllSourceData', view_func=FilterAsSource.as_view('fetchAllSourceData'))
app.add_url_rule('/fetchAllSourceDataStudentId', view_func=FilterAsSourceStudentId.as_view('fetchAllSourceDataStudentId'))
