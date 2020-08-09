from django.shortcuts import render
# from .models import Project

# Create your views here.
def base(request):
    context={}
    return render(request,'cov/base.html',context)

