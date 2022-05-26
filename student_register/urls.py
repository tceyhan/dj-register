
from django.urls import path
from django.views.generic.base import TemplateView
from student_register.views import StudentCreateView, StudentListView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path("", TemplateView.as_view(template_name='student_register/student_form.html'), name='home'),
    path("form/",StudentCreateView.as_view(), name="form"),  
    path("list/",StudentListView.as_view(), name="list"),
    path("update/<int:pk>/",StudentUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/",StudentDeleteView.as_view(), name="delete"), 
]
