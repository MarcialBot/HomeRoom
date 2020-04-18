from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Classroom
from .forms import ProfileForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def classroom_index(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classroom/classroom-list.html', {'classrooms': classrooms})

def classrooms_detail(request, classroom_id):
    classroom = Classroom.get(id=classroom_id)
    return render(request, 'classroom/detail.html', {
        'classroom': classroom
    })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    profile_form = ProfileForm()
    context = {'form': form, 'profile_form': profile_form,
               'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class ClassroomCreate(CreateView):
    model = Classroom
    fields = ['subject', 'description']
    success_url = '/classrooms/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ClassroomList(ListView):
    model = Classroom
