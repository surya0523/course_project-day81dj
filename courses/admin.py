from django.contrib import admin
from .models import Course, Teacher, Lesson

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Lesson)