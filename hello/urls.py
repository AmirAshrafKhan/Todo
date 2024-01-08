
from django.urls import path
from . import views 
urlpatterns = [
    path("", views.index, name="index"),
    path("amir", views.amir, name="amir"),
    path("<str:name>", views.greet, name="greet")
]