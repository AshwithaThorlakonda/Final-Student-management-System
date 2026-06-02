from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            roll_no=request.POST['roll_no'],
            email=request.POST['email'],
            department=request.POST['department']
        )
        return redirect('/')

    return render(request, 'add_student.html')

