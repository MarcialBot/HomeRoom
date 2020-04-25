import logging
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect

from .models import Classroom, Assignment
from .forms import ProfileForm, ExtendedUserForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def classroom_index(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classroom/classroom-list.html', {'classrooms': classrooms})


@login_required
def classrooms_detail(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    assignment = Assignment.objects.all()
    return render(request, 'classroom/classroom-detail.html', {
        'classroom': classroom, 'assignment': assignment
    })


def signup(request):
    if request.method == 'POST':
        form = ExtendedUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/signup.html', {'form': form, 'profile_form': profile_form})
    form = ExtendedUserForm()
    profile_form = ProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/signup.html', context)


class ClassroomCreate(LoginRequiredMixin, CreateView):
    model = Classroom
    fields = ['subject', 'description']
    success_url = '/classrooms/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClassroomUpdate(LoginRequiredMixin, UpdateView):
    model = Classroom
    fields = ['subject', 'description']


class ClassroomDelete(LoginRequiredMixin, DeleteView):
    model = Classroom
    success_url = '/classrooms/'


class AssignmentCreate(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = ['name', 'description', 'grade', 'due_date']

    def form_valid(self, form):
        form.instance.classroom_id = self.kwargs.get('pk')
        return super(AssignmentCreate, self).form_valid(form)


class AssignmentUpdate(LoginRequiredMixin, UpdateView):
    model = Assignment
    fields = ['name', 'description', 'grade', 'due_date']
    success_url = '/assigments/'


class AssignmentDelete(LoginRequiredMixin, DeleteView):
    model = Assignment
    success_url = '/assigments/'


class AssignmentList(LoginRequiredMixin, ListView):
    model = Assignment


class AssignmentDetail(LoginRequiredMixin, DetailView):
    model = Assignment
