from django.shortcuts import render, HttpResponse
from .models import Contact 

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is the about page.")

def services(request):
    return HttpResponse("This is the services page.")

def index(request):
    if request.method == "POST":
        contact=Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comments')
        contact.name=name
        contact.email=email
        contact.comment=comment
        contact.save()
        return HttpResponse("<h1>Thanks for contacting us</h1>")
    return render(request, 'contact.html')

def inbox(request):
    return render(request,'login.html')
