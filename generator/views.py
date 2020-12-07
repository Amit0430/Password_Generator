from django.shortcuts import render, HttpResponse
import random
import string

def home(request):
    return render(request, 'generator_pages/home.html')

def password(request):

    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)



    return render(request, 'generator_pages/password.html', {'password':the_password})


def about(request):
    return render(request, 'generator_pages/about.html')