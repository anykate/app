from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('students/', views.home, name='home'),
    path('students/<int:student_id>/', views.detail, name='students_detail'),
]
