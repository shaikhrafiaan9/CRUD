from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView ,CreateView , UpdateView , DeleteView
from basic_app.models import School , Student
from django.urls import reverse_lazy
# Create your views here.



class CBView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Hello This is Template View '
        return context



class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    model = School
    fields = ('name','principal','location')

class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name','principal','location')


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("basic_app:list")

class StudentCreateView(CreateView):
    model = Student
    fields = ('name','age','school')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('name','age','school')

class StudentListView(ListView):
    model = Student
    context_object_name = 'students_list'


class StudentDetailView(DetailView):
    model = Student
    fields = ('name','age','school')
    template_name = 'basic_app/student_detail.html'
