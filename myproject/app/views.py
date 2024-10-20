from django.forms import formset_factory
from .forms import CourseForm, CoursePointForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Course, Point
from django.shortcuts import get_object_or_404


def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)  # Створення форми курсу з даними POST
        points = request.POST.getlist('points')  # Отримання всіх полів пунктів

        if course_form.is_valid():  # Перевірка на валідність форми курсу
            course = course_form.save()  # Збереження курсу

            # Збереження пунктів
            for content in points:
                if content:  # Перевірка на пусті значення
                    Point.objects.create(course=course, content=content)  # Створення нового об'єкта Point

            return redirect('course_list')  # Перенаправлення на список курсів
    else:
        course_form = CourseForm()  # Порожня форма при GET-запиті

    return render(request, 'courses/add_course.html', {'course_form': course_form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        points = request.POST.getlist('points')  # Отримання всіх вибраних пунктів
        # Оновлення стану завершення для кожного пункту
        for point in course.points.all():
            point.completed = str(point.id) in points  # Встановлення статусу на основі вибору чекбоксів
            point.save()  # Збереження змін

        return redirect('course_list')  # Перенаправлення на список курсів

    return render(request, 'courses/course_detail.html', {'course': course})
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Отримати курс або 404, якщо не знайдено
    course.delete()  # Видалення курсу
    return redirect('course_list')