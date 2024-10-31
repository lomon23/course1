
from .forms import CourseForm
from django.http import HttpResponse
from .models import Course, Point
from django.shortcuts import get_object_or_404
import MySQLdb
from django.shortcuts import render, redirect

def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)  # Створення форми курсу з даними POST
        points = request.POST.getlist('points')  # Отримання всіх полів пунктів

        if course_form.is_valid():  # Перевірка на валідність форми курсу
            course = course_form.save(commit=False)  # Не зберігаємо ще в базу
            course.save()  # Збереження курсу

            # Збереження пунктів
            for point_content in points:
                if point_content:  # Перевірка на пусті значення
                    Point.objects.create(course=course, content=point_content)  # Створення нового об'єкта Point

            return redirect('course_list')  # Перенаправлення на список курсів
    else:
        course_form = CourseForm()  # Порожня форма при GET-запиті

    return render(request, 'add_course.html', {'course_form': course_form})
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        points = request.POST.getlist('points')  # Отримання всіх вибраних пунктів
        # Оновлення стану завершення для кожного пункту
        for point in course.points.all():
            point.completed = str(point.id) in points  # Встановлення статусу на основі вибору чекбоксів
            point.save()  # Збереження змін

        return redirect('course_list')  # Перенаправлення на список курсів

    return render(request, 'course_detail.html', {'course': course})
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Отримати курс або 404, якщо не знайдено
    course.delete()  # Видалення курсу
    return redirect('course_list')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Підключаємося до бази даних
        db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="lo123TAV", db="my_database")
        cursor = db.cursor()

        # Вставка даних у таблицю
        sql = "INSERT INTO users (first_name, last_name, username, email, password) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (first_name, last_name, username, email, password))

        db.commit()
        db.close()

        return redirect('/login/')  # Перенаправляємо на сторінку логіну після реєстрації

    return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Підключаємося до бази даних
        db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="lo123TAV", db="my_database")
        cursor = db.cursor()

        # Перевірка користувача в базі даних
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()

        db.close()

        if user:
            request.session['user_id'] = user[0]  # Зберігаємо ID користувача в сесії
            return redirect('/')  # Перенаправляємо на закриту сторінку
        else:
            return HttpResponse("Invalid login details.")

    return render(request, 'login.html')
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')