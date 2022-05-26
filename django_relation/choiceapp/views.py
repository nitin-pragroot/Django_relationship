from django.shortcuts import redirect, render

from .models import Student

# Create your views here.
def home(request):
    return render(request, "index.html")

def student(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']
        city = request.POST['city']
        semester = request.POST['semester']
        stu = Student.objects.create(name=name, age=age, course=course, city=city,semester=semester)
        stu.save()
        return redirect("/")
    else:
        return render(request, 'index.html')