from django.shortcuts import redirect, render

from app.models import Car

def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})

def developers(request):
    if request.user.is_authenticated:
        return render(request, 'developers.html')
    
    return redirect('/admin/login/?next=/')