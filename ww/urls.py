from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='student_list'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('create/', views.student_create, name='student_create'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]
