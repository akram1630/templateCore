from django.urls import path
from . import views

app_name = 'student'  #necessary for navigation

urlpatterns = [  # name is used in href =
    path('', views.all_students, name='allStudents'),  #name= for navigation
    path('add/', views.add_student, name='addStudent'),
    path('edit/', views.edit_student, name='editStudent')
]
