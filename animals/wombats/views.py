from django.shortcuts import HttpResponse

# main view (like index.html)
#  path is '/'
def home(request):
    message = "Hello, UMBC Django world"
    return HttpResponse(message)

def lunch(request):
    return HttpResponse("Lunch is at 12 Noon")

