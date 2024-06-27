from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest,JsonResponse
def home (request):
    data ={
        "name=": "vivek",
        "age": "22",
        "address" : "satna"
    }

    return JsonResponse(data)
def register (request):
    return render(request,'register.html')

    
