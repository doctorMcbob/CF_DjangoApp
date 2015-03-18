from django.http import HttpRequest
from django.core import validators
from django.shortcuts import render
from django import forms
from usradmin.models import BasicUser

def edit_user(request):
    usr = BasicUser.objects.get(pk=request.GET['id'])
    if request.GET['first']:
        usr.first = request.GET['first']
    if request.GET['last']:
        usr.last = request.GET['last']
    if request.GET['email']:
        usr.email = request.GET['email']
    usr.save()
    return render(request, 'show_users.html')
    
def delete_user(request):
    usr = BasicUser.objects.get(pk=request.GET['id'])
    usr.delete()
    return render(request, 'show_users.html')

def create_user(request):
    error=False
    usr = BasicUser(first=request.GET['first'], last=request.GET['last'], email=request.GET['email'])
    if not usr.first:
        error = True
    try:
         validators.validate_email(usr.email)
    except forms.ValidationError:
        error = True
    if not error:
        usr.save()
    return render(request, 'show_users.html',
                  {'error':error})
