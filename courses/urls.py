from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('', views.course_list, name='course_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('teacher/<int:pk>/', views.teacher_detail, name='teacher_detail'),
]