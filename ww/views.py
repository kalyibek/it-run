from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models


class StudentsListView(ListView):
    model = models.Student
    template_name = 'ww/students.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = models.Student
    template_name = 'ww/student.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = models.Student
    template_name = 'ww/student_create.html'
    fields = ['first_name', 'last_name', 'age', 'description', 'photo', 'klass']
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['klasses'] = models.Klass.objects.all()
        return context


class StudentUpdateView(UpdateView):
    model = models.Student
    template_name = 'ww/student_update.html'
    fields = ['first_name', 'last_name', 'age', 'description', 'photo', 'klass']
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['klasses'] = models.Klass.objects.all()
        return context


class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy('student_list')
