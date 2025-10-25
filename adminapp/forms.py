from django import forms
from .models import *


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        labels = {
            "name": "Faculted nomi",
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class KafedraForm(forms.ModelForm):
    class Meta:
        model = Kafedra
        fields = "__all__"
        labels = {
            "name": "Kafedra nomi",
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "faculty": forms.Select(attrs={'class': 'form-select'})
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        labels = {
            "name": "Fan nomi ",
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "kafedra": forms.Select(attrs={'class': 'form-select'})
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        labels = {
            "full_name": "Ustozning ismi",
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "subjects": forms.Select(attrs={'class': 'form-select'})
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
        labels = {
            "name": "Gurux nomi",
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "subject": forms.Select(attrs={'class': 'form-select'})
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "full_name": "Talaba ismi",
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "group": forms.Select(attrs={'class': 'form-select'})
        }