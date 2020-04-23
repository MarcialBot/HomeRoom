from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Classroom, Assignment


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type', 'address', 'phone_number')


class ClassForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['subject', 'user']


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['name', 'description', 'grade', 'due_date']
