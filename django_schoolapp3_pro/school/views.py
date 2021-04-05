from django.shortcuts import render, redirect
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
    # if get return create.html page
    # else create a school from the user posted info
