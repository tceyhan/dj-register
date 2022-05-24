
from django.urls import path
from django.views.generic.base import TemplateView
from student_register.views import StudentCreateView, StudentListView

urlpatterns = [
    path('', TemplateView.as_view(template_name='student_register/student_form.html'), name='home'),
    path("form/",StudentCreateView.as_view(), name="form"),  
    path("list/",StudentListView.as_view(), name="list"),  
]
