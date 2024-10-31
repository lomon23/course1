from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_course, name='add_course'),    path('', views.course_list, name='course_list'),  # Головна сторінка для списку курсів
    path('delete_course/<int:course_id>/', views.delete_course,name='delete_course'),  # Видалення курсу

    path('course/<int:course_id>/', views.course_detail, name='course_detail'),  # Деталі курсу
]