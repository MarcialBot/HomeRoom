from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('classrooms/', views.classroom_index, name='classrooms_index'),
    path('classrooms/<int:classroom_id>/',
         views.classrooms_detail, name='classroom_detail'),
    path('classrooms/create/', views.ClassroomCreate.as_view(),
         name='classrooms_create'),
    path('assignments/create/', views.AssignmentCreate.as_view(),
         name='assignments_create'),
    path('assignments/', views.AssignmentList.as_view(), name='assignments_index'),
    path('accounts/signup/', views.signup, name='signup'),
]
