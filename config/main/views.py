from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index():
    return HttpResponse('Hello World')

def set_cookie(request):
    response = HttpResponse("Cookie o‘rnatildi!")
    response.set_cookie('user', 'hello world', max_age=3600)
    return response

def get_cookie(request):
    user = request.COOKIES.get('user', 'Cookie topilmadi!')
    return HttpResponse(f"Cookie qiymati: {user}")

def delete_cookie(request):
    response = HttpResponse("Cookie o‘chirildi!")
    response.delete_cookie('user')
    return response
