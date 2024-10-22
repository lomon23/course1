from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models

class Point(models.Model):
    course = models.ForeignKey(Course, related_name='points', on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    material_type = models.CharField(max_length=20, blank=True)  # Поле для зберігання типу матеріалу
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.content
