from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Well, it's a start...")

