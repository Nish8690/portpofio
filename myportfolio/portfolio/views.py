from django.shortcuts import render
from .models import Project
from math import ceil
# Create your views here.
def base(request):

    context={}
    return render(request,'pf/home.html',context)

def home(request):
    return render(request,'pf/home.html')

def aboutme(request):
    return render(request,'pf/aboutme.html')

def projects(request):
    # projects=Project.objects.all()
    # n=len(projects)
    # print(n)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # context={'no. of slides':nSlides,'range':range(1, nSlides) ,'projects': projects}
    # context={'project_name': proj_name}

    allProjs=[]
    catprojs = Project.objects.values('category')
    cats={item['category'] for item in catprojs}
    for cat in cats:
        proj=Project.objects.filter(category=cat)
        n=len(proj)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProjs.append([proj,range(1,nSlides),nSlides])
    context={'allProjs': allProjs}
    return render(request,'pf/projects.html',context)

def contactme(request):
    return render(request,'pf/contactme.html')

def resume(request):
    return render(request,'pf/resume.html')

def documents(request):
    return render(request,'pf/documents.html')
