from applications import app
from applications.user.views import *
from applications.restaurant.views import *
from applications.foodList.views import *
from applications.cart.views import *
from applications.paymentDetail.views import *

# USER
app.add_url_rule("/", view_func=UserRegister.as_view(""))
app.add_url_rule("/register-new-user", view_func=UserRegister.as_view("registerNewUser"))
app.add_url_rule("/login-user", view_func=UserLogin.as_view("loginUser"))
app.add_url_rule("/update-user/<int:id>", view_func=UserEdit.as_view("updateUser"))
app.add_url_rule("/delete-user-account/<int:id>", view_func=UserEdit.as_view("deleteUserAccount"))

# RESTAURANT
app.add_url_rule("/add-restaurant", view_func=Restaurant.as_view("addRestaurant"))
app.add_url_rule("/fetch-all-restaurant", view_func=Restaurant.as_view("/fetchAllRestaurants"))

# FOOD-LIST
app.add_url_rule("/add-food", view_func=Food.as_view("addFood"))
app.add_url_rule("/get-food-list/<string:restaurant>", view_func=Food.as_view("getFoodList"))

# CART
app.add_url_rule("/get-food", view_func=Cart.as_view("getFood"))
app.add_url_rule("/add-cart", view_func=Cart.as_view("addCart"))

# PAYMENT DETAIL
app.add_url_rule("/add-payment", view_func=Payment.as_view("payment"))
app.add_url_rule("/delete-all/<int:id>", view_func=Payment.as_view("deleteAll"))
