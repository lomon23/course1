from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.CharField(max_length=10, null=True, help_text="Введіть дату у форматі YYYY-MM-DD")  # Поле для дедлайну, яке може бути пустим

    def __str__(self):
        return self.name  # Це зручно для перегляду в адмінці
class Point(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='points')
    content = models.TextField()

    def __str__(self):
        return self.content  # Це зручно для перегляду в адмінці
