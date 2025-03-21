from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello World')

def add_to_session(request):
    request.session['username'] = 'Asilbek'
    request.session['role'] = 'bankir'
    return HttpResponse("Sessiyaga ma'lumot qo'shildi.")


def view_session(request):
    username = request.session.get('username', 'Mavjud emas')
    role = request.session.get('role', 'Mavjud emas')
    return HttpResponse(f"Foydalanuvchi: {username}, Rol: {role}")

def update_session(request):
    request.session['role'] = 'senior developer'
    return HttpResponse("Sessiya ma'lumotlari o'zgartirildi.")

def delete_session(request):
    request.session.flush()
    return HttpResponse("Sessiya o'chirildi.")


