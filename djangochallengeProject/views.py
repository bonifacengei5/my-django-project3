from django.shortcuts import render
from .models import Students

def home(request):
    return render, (request, 'index.html')

def add_students(request):
    if request.method == "POST":
        s_name = request.POST.get("s-name")
        s_email = request.POST.get("s-Email")
        s_age = request.POST.get("s-Age")

        context = {
            "s_name": s_name,
            "s_Email": s_email,
            "S_age": s_age,

            "success": "Successful registration"
        }

        query = Students(name=s_name, email=s_email,
                         age=s_age)
        query.save()

    return render(request, 'addstudents.html')

def students(request):
    all_students = Students.objects.all()
    context = {"all_students": all_students}

    return render(request, 'students.html', context)
