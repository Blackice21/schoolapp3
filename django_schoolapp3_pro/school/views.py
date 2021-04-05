from django.shortcuts import render, redirect, get_object_or_404
from .models import School
from .forms import SchoolForm
# Create your views here.

def home(request):
    schools = School.objects.all()
    return render(request, 'home.html',{'schools': schools})

def create(request):
    # check if method is post or get
    if request.method == 'GET':
        schoolform = SchoolForm()
        return render(request, 'create.html', {'schoolform': SchoolForm})
    else:
        schoolform = SchoolForm(request.POST, request.FILES)
        schoolform.save()
        return redirect('home')

def update_school(request, pk):
    # check if request is get or post
    school = get_object_or_404(School, pk=pk)
    if request.method == 'GET':
        schoolform = SchoolForm(instance=school)
        return render(request, 'update.html', {'schoolform': schoolform, 'school':school})
    else:
        schoolform = SchoolForm(request.POST, request.FILES, instance=school)
        schoolform.save()
        return redirect('home')
    # if get then return update.html page
    # else update specific school, redirect to home

def delete_school(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'school':school})
    else:
        school.delete()
        return redirect('home')

def detail_school(request,pk):
     school = get_object_or_404(School, pk=pk)   
     return render(request, 'detail.html', {'school': school})
  
