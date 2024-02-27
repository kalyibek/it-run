from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from . import models


class StudentsListView(View):
    students: tuple

    def get(self, request):
        self.students = models.Student.objects.all()
        return render(
            request,
            'ww/students.html',
            {'students': self.students}
        )


class StudentDetailView(View):
    student: models.Student

    def get(self, request, pk):
        self.student = get_object_or_404(models.Student, pk=pk)
        return render(
            request,
            'ww/student.html',
            {'student': self.student}
        )


class StudentCreateView(View):
    klasses: tuple
    student: models.Student

    def get(self, request):
        self.klasses = models.Klass.objects.all()
        return render(
            request,
            'ww/student_create.html',
            {'klasses': self.klasses}
        )

    def post(self, request):
        self.student = models.Student.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            age=request.POST['age'],
            description=request.POST['description'],
            photo=request.FILES['photo'],
            klass=get_object_or_404(models.Klass, pk=request.POST['klass'])
        )
        self.student.save()
        return redirect('/')


class StudentUpdateView(View):
    klasses: tuple
    student: models.Student

    def get(self, request, pk):
        self.student = get_object_or_404(models.Student, pk=pk)
        self.klasses = models.Klass.objects.all()
        return render(
            request,
            'ww/student_update.html',
            {'klasses': self.klasses, 'student': self.student}
        )

    def post(self, request, pk):
        self.student = get_object_or_404(models.Student, pk=pk)
        self.student.first_name = request.POST['first_name']
        self.student.last_name = request.POST['last_name']
        self.student.age = request.POST['age']
        self.student.description = request.POST['description']
        self.student.photo = request.FILES['photo']
        self.student.klass = get_object_or_404(models.Klass, pk=request.POST['klass'])
        self.student.save()
        return redirect('/')


class StudentDeleteView(View):
    student: models.Student

    def get(self, request, pk):
        self.student = get_object_or_404(models.Student, pk=pk)
        self.student.photo.delete()
        self.student.delete()
        return redirect('/')

