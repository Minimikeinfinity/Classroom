from django.http import HttpResponse

def index(request):
    return HttpResponse("Bottom of page")