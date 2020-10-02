from django.urls import path, include, re_path
from app.views import car_list

app_name = 'app'

urlpatterns = [
    path('', car_list, name='index'),
    ]