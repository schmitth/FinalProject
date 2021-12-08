from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from PW_House.forms import SourceForm
from .models import sourceTable


# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return login_view(request)


@login_required(login_url='login')
def images_view(request):
    return render(request, 'images.html')


@login_required(login_url='login')
def read_view(request):
    sources = sourceTable.objects.all()
    context = {'sources': sources}
    return render(request, 'sources.html', context)


@login_required(login_url='login')
def create_view(request):
    form = SourceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'sources.html')
    return render(request, 'sources-form.html', {'form': form})


@login_required(login_url='login')
def update_view(request, id):
    source = sourceTable.objects.get(id=id)
    form = SourceForm(request.POST or None, instace=source)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request, 'sources-form.html', {'form': form})


@login_required(login_url='login')
def delete_view(request, id):
    source = sourceTable.objects.get(id=id)
    if request.method == 'POST':
        source.delete()
        return redirect('read')
    return render(request, 'delete-confirm.html', {'Source': source})
