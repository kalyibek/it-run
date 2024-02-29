from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentsListView.as_view(), name='student_list'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('create/', views.StudentCreateView.as_view(), name='student_create'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
]
