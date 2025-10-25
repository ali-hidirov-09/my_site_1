from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Faculty.name, on_delete=models.CASCADE, related_name="kafedralar")

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    kafedra = models.ForeignKey(Kafedra.name, on_delete=models.CASCADE, related_name="fanlar")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    kafedra = models.ForeignKey(Kafedra.name, on_delete=models.CASCADE, related_name="t_kafedra")
    subjects = models.ManyToManyField(Subject.name, related_name="t_subject")

    def __str__(self):
        return self.full_name


class Group(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject.name, related_name="g_subject")

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group.name, on_delete=models.CASCADE, related_name="st_group")

    def __str__(self):
        return self.full_name