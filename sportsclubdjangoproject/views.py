from django.shortcuts import render

def index(request):
       return render(request,"index.html")

def about(request):
       return render(request,"about.html")

def contact(request):
       return render(request,"contact.html")

def games(request):
       return render(request,"games.html")

def tranner(request):
       return render(request,"tranner.html")
