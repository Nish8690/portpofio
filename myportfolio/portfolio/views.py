from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'pf/base.html')

def home(request):
    return render(request,'pf/home.html')

def aboutme(request):
    return render(request,'pf/aboutme.html')

def projects(request):
    return render(request,'pf/projects.html')

def contactme(request):
    return render(request,'pf/contactme.html')

def resume(request):
    return render(request,'pf/resume.html')
