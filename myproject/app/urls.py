from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('add/', views.add_course, name='add_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]