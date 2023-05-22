from django.shortcuts import render, HttpResponse

# Create your views here.

# Create your views here.
def home(request):
    return render(request, 'home.html')

def no(request):
    return render(request,'no.html')

def yes(request):
    return render(request,'yes.html')