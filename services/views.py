from django.http import HttpRequest, HttpResponse

def greetings(request: HttpRequest):
    return HttpResponse("Hello world")
