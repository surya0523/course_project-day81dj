from django.db import models
from django.contrib.auth.models import User

# Teacher Model with ManyToMany relationship to Course
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    
    # ManyToMany relationship for reverse access: teacher.courses.all()
    courses = models.ManyToManyField('Course', related_name='teachers')
    
    def __str__(self):
        return self.name

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# Lesson Model with ForeignKey relationship to Course
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    # ForeignKey for reverse access: course.lessons.all()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f"{self.title} ({self.course.title})"