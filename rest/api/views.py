from django.shortcuts import render
from django.db.models import Q
from .models import Student

# Create your views here.
def home(request):
    # stud = Student.objects.all()
    # stud = Student.objects.filter(Q(id=1) | Q(id=3))
    # stud = Student.objects.filter(Q(id=1) & Q(phone=7903511479))
    stud = Student.objects.filter(~Q(id=1) & ~Q(id=3))
    print("return" , stud)
    return render(request , 'home.html' , {'student':stud})

    
