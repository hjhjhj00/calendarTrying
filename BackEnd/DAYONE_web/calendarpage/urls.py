from django.urls import path
from . import views

app_name = "calendarpage"
urlpatterns = [
  path('', views.index, name='index'),
]