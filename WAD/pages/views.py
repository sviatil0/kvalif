from django.shortcuts import render
from esp32 import forms
from esp32.forms import EspForm
from esp32.models import ESP
from django.http import HttpResponseRedirect
# Create your views here.


def homepage_view(request, *args, **kwargs):
    return render(request, "home.html")

def add_view(request):
    form = EspForm(request.POST or None)
    esp = ESP.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form': form})

def show_view(request):
    esp = ESP.objects.all()
    return render(request, 'show.html', {'esp':esp})


def update_view(request, id):
    esp = ESP.objects.get(id = id)
    form = EspForm(request.POST, instance=esp)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'esp':esp})

def delete_view(request, id):
    form = ESP.objects.get(id=id)

    form.delete()
    return HttpResponseRedirect('/')
def turn_on_view(request,id):
    esp = ESP.objects.get(id = id)
    ESP.objects.filter(id=id).update(mode = True)
    return HttpResponseRedirect('/')

def turn_off_view(request,id):
    esp = ESP.objects.get(id = id)
    ESP.objects.filter(id=id).update(mode = False)
    return HttpResponseRedirect('/')
