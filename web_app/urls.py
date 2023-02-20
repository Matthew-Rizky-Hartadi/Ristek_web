from django.urls import path
from web_app.views import show_home, show_profile

app_name = 'web_app'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('profile', show_profile, name='show_profile')
]