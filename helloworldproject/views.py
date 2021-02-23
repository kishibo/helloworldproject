from django.http import HttpResponse
from django.views.generic import TemplateView #3-9

def helloworldfunc(request):
    responseobject = HttpResponse('<h1>hello world</h1>')
    return responseobject

class HelloWorldClass(TemplateView): #3-9
    template_name = 'hello.html'

