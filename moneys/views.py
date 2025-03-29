from django.shortcuts import render, redirect
from .models import Folder, AddMoney

def home(request):
    if request.user:
        folders = Folder.objects.filter(user=request.user)
        addmoneys = AddMoney.objects.filter(user=request.user)
        context = {
            'folders': folders,
            'addmoneys': addmoneys,
        }
    else:
        context = {}
    return render(request, 'index.html', context)