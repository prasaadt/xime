from django.shortcuts import render
from django.http import HttpResponse
from students.models import students

# Create your views here.
def slogin(request):
    return render(request,'slogin.html')
def studentview(request):
    students_list=students.objects.order_by('sname')
    my_dict={'students_list':students_list}
    return render(request,'student.html',context=my_dict)