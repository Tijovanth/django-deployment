from django.urls import path
from exampleapp import views

app_name = 'exampleapp'

urlpatterns = [
path(r'register/',views.register,name='register'),
]
