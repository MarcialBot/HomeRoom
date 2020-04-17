from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return f" Username: {self.user} | Subject: {self.subject}"
