from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def base(request):
    context = { }
    return render(request,'base.html')