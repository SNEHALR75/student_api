from django.urls import path
from .api import StudentAPI,StudentDetailAPI


urlpatterns = [

    path('student/',StudentAPI.as_view()),
    path('student/<pk>/',StudentDetailAPI.as_view()),
]