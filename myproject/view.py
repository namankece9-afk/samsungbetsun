from django.http import HttpResponse

def index(request):
    return HttpResponse("Halo Dunia dari Django")