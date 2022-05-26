from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_register/student_form.html'
    success_url = reverse_lazy('home')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_register/student_list.html'
    context_object_name = 'students'
    # def get_queryset(self):
    #     return Student.objects.filter(id=self.kwargs['pk'])
    # def delete(self, request, *args, **kwargs):
    #     self.get_queryset().delete()
    #     return redirect('home')

    