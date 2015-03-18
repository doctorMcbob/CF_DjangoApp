from django.shortcuts import render
from usradmin.models import BasicUser

def basicglobal(request):
    return {"users":BasicUser.objects.all()}

# Create your views here.

def home(request):
    return render(request, 'show_users.html',
                  {"error":False})

def edit(request, usrid):
    return render(request, 'edit_user.html',
                  {"user":BasicUser.objects.get(id=int(usrid))})
                
