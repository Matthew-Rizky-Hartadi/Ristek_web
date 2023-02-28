from django.urls import path
from web_app.views import *

app_name = 'web_app'

urlpatterns = [
    path('home', show_home, name='show_home'),
    path('profile', show_profile, name='show_profile'),
    path('', non_user_home, name="non_user_home"),
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('json',show_data_json,name="json"),
    path('add_post', add_post, name="add_post"),
    path('add_post2', add_post2, name="add_post2"),
    path('logout', logout_user, name='logout'),
    path('delete/<int:id>', delete_post, name='delete'),
    path('deleteA/<int:id>', delete_A, name='delete_A'),
    path('deleteU/<int:id>', delete_User, name='delete_U'),
    path('edit_post/<int:id>', edit_post, name='edit_post'),

]