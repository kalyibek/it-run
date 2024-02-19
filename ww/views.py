import os
from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


def students_list(request):
    students = models.Student.objects.all()
    return render(
        request,
        'ww/students.html',
        {'students': students}
    )


def student_detail(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    return render(
        request,
        'ww/student.html',
        {'student': student}
    )


def student_create(request):
    if request.method == 'POST':
        student = models.Student.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            age=request.POST['age'],
            description=request.POST['description'],
            photo=request.FILES['photo'],
            klass=get_object_or_404(models.Klass, pk=request.POST['klass'])
        )
        student.save()
        return redirect('/')

    klasses = models.Klass.objects.all()
    return render(
        request,
        'ww/student_create.html',
        {'klasses': klasses}
    )


def student_delete(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    student.photo.delete()
    student.delete()
    return redirect('/')


def student_update(request, pk):
    if request.method == 'POST':
        klass = models.Klass.objects.get(pk=request.POST['klass'])
        student = models.Student.objects.filter(pk=pk).update(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            klass=klass,
            age=request.POST['age'],
            description=request.POST['description']
        )
        old_photo = models.Student.objects.get(pk=pk)
        form = forms.ImageForm(request.POST, request.FILES, instance=old_photo)
        if form.is_valid():
            image_path = old_photo.photo.path
            if os.path.exists(image_path):
                os.remove(image_path)
            form.save()

        return redirect('/')

    last_student = models.Student.objects.get(pk=pk)
    klasses = models.Klass.objects.all()
    context = {
        'last_student': last_student,
        'klasses': klasses
    }

    return render(request, 'ww/student_update.html', context)
