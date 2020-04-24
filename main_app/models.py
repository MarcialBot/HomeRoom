from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone

from django.contrib.auth.models import User

USER_TYPES = (
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPES,
        default='student'
    )
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()

    def __str__(self):
        return f" Username: {self.user} | Usertype: {self.get_user_type_display()}"


class Classroom(models.Model):
    subject = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(
        max_length=500, default='Enter A Description')

    def __str__(self):
        return f" Username: {self.user} | Subject: {self.subject}"

    def get_absolute_url(self):
        return reverse('classroom_detail', kwargs={'classroom_id': self.id})


class Assignment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    grade = models.IntegerField(default=0)
    date_created = models.DateField(default=timezone.now)
    due_date = models.DateField('due date')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f" Subject: {self.classroom.subject} | Assignment: {self.name}"

    def get_absolute_url(self):
        return reverse('classroom_detail', kwargs={'classroom_id': self.classroom.id})


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()
