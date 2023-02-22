from django.urls import path
from web_app.views import show_home, show_profile, non_user_home, register, login_user,show_data_json, add_post, add_post2

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

]