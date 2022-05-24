from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Student
from student_register.forms import StudentForm
from django.urls import reverse_lazy
# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_register/student_form.html'
    success_url = reverse_lazy('home')

class StudentListView(ListView):
    model = Student
    template_name = 'student_register/student_list.html'
    context_object_name = 'students'
    