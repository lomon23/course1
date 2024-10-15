from django import forms
from .models import Course, Point

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class CoursePointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Введіть пункт'}),
        }
