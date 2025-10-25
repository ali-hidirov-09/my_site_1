from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from adminapp.forms import *
from adminapp.models import Faculty, Kafedra
from .services import *


def login_required_decorator(func):
    """teksirish"""
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    """chiqish uchun"""
    logout(request)
    return redirect("login_page")


def login_page(request):
    """lig in qiluvchi oyna"""
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')


@login_required_decorator
def home_page(request):
    """ asosiy bet"""
    faculties = get_faculties()
    kafedras = get_kafedra()
    ctx = {
        'counts': {
        "faculties": len(faculties),
        "kafedras": len(kafedras)
        }
    }
    return render(request, 'index.html', ctx)


class SignUpView(generic.CreateView):
    """Sign up qilish"""
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = "signup.html"


"""FACULTED"""
@login_required_decorator
def faculty_create(request):
    """ faculted yaratadigan funcsiya """
    model = Faculty()
    form = FacultyForm(request.POST, instance=model)  # modelga saqlaydi
    if request.POST and form.is_valid():
        form.save()
        return redirect("faculty_list")
    ctx = {
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)



@login_required_decorator
def faculty_edit(request, pk):
    """faculted nomini ozgartirish uchun"""
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        'model': model,
        'form':form,
    }
    return render(request, 'faculty/form.html', ctx)

@login_required_decorator
def faculty_delete(request, pk):
    """facultedni ochirish uchun"""
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')


@login_required_decorator
def faculty_list(request):
    """ Facultedlar listini chiqaradi"""
    faculties = get_faculties()
    ctx = {
        'faculties':faculties,
    }
    return  render(request, 'faculty/list.html', ctx)


"""Kafedra"""
@login_required_decorator
def kafedra_create(request):
    """ Kafedra yaratish"""
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("kafedra_list")
    ctx = {
        "form":form
    }
    return  render(request, "kafedra/form.html", ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    """ Kafedralarni ozgartirish """
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("kafedra_list")
    ctx = {
        "model": model,
        "form": form
    }
    return  render(request, "kafedra/form.html", ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    """ Kafedralarni o'chirish"""
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return  redirect('kafedra_list')


@login_required_decorator
def kafedra_list(request):
    """ Kafedralar listini chiqaradi"""
    kafedras = get_kafedra()
    ctx = {
        "kafedras": kafedras
    }
    return render(request, "kafedra/list.html", ctx)





