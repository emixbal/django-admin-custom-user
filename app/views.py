from django.http import HttpResponse

def version(request):
    version = 'v0.7'
    return HttpResponse(version)
