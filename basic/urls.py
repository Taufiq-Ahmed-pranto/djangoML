from django.urls import path
from .import views

urlpatterns = [
    path('', views.hello, name="hello"),
    path('user', views.user, name="user")
]
