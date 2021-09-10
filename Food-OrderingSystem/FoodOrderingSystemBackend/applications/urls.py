from applications import app
from applications.user.views import *



# USER
app.add_url_rule('/registerNewUser', view_func=UserReg.as_view('registerNewUser'))
app.add_url_rule('/LoginUser', view_func=UserLogin.as_view('LoginUser'))
