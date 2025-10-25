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


"""Subject"""
@login_required_decorator
def subject_create(request):
    """ subject yaratish"""
    model = Subject
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("subject_list")
    ctx = {
        "form":form
    }
    return  render(request, "subject/form.html", ctx)


@login_required_decorator
def subject_delete(request, pk):
    """ fanlarni o'chirish"""
    model = Subject.objects.get(pk=pk)
    model.delete()
    return  redirect('subject_list')


@login_required_decorator
def subject_edit(request, pk):
    """ subjectlarni ozgartirish """
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("subject_list")
    ctx = {
        "model": model,
        "form": form
    }
    return  render(request, "subject/form.html", ctx)


@login_required_decorator
def subject_list(request):
    """ subjectlar listini chiqaradi"""
    subjects = get_subject()
    ctx = {
        "subjects": subjects
    }
    return render(request, "subject/list.html", ctx)


"""Teacher"""
@login_required_decorator
def teacher_list(request):
    """ o'qituvchilar listini chiqaradi"""
    teachers = get_teacher()
    ctx = {
        "teachers": teachers
    }
    return render(request, "teacher/list.html", ctx)


@login_required_decorator
def teacher_edit(request, pk):
    """ o'qituvchilarni ozgartirish """
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("teacher_list")
    ctx = {
        "model": model,
        "form": form
    }
    return  render(request, "teacher/form.html", ctx)


@login_required_decorator
def teacher_create(request):
    """ teacher qo'shish"""
    model = Teacher
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("teacher_list")
    ctx = {
        "form":form
    }
    return  render(request, "teacher/form.html", ctx)


@login_required_decorator
def teacher_delete(request, pk):
    """ o'qituvchini o'chirish"""
    model = Teacher.objects.get(pk=pk)
    model.delete()
    return  redirect('teacher_list')


"""Group"""
@login_required_decorator
def group_create(request):
    """ gruppa qo'shish"""
    model = Group
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("group_list")
    ctx = {
        "form":form
    }
    return  render(request, "group/form.html", ctx)


@login_required_decorator
def group_delete(request, pk):
    """ gruppani o'chirish"""
    model = Group.objects.get(pk=pk)
    model.delete()
    return  redirect('group_list')


@login_required_decorator
def group_edit(request, pk):
    """ gruppalarni ozgartirish """
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("group_list")
    ctx = {
        "model": model,
        "form": form
    }
    return  render(request, "group/form.html", ctx)


@login_required_decorator
def group_list(request):
    """ gruppalar listini chiqaradi"""
    groups = get_group()
    ctx = {
        "groups": groups
    }
    return render(request, "group/list.html", ctx)


"""Student"""
@login_required_decorator
def student_list(request):
    """ studentlar listini chiqaradi"""
    students = get_student()
    ctx = {
        "students": students
    }
    return render(request, "student/list.html", ctx)


@login_required_decorator
def student_edit(request, pk):
    """ studentlarni ozgartirish """
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("student_list")
    ctx = {
        "model": model,
        "form": form
    }
    return  render(request, "student/form.html", ctx)

@login_required_decorator
def student_create(request):
    """ student qo'shish"""
    model = Student
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("student_list")
    ctx = {
        "form":form
    }
    return  render(request, "student/form.html", ctx)


@login_required_decorator
def student_delete(request, pk):
    """ gruppani o'chirish"""
    model = Student.objects.get(pk=pk)
    model.delete()
    return  redirect('student_list')


