from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    teachers = models.ManyToManyField(Teacher, related_name='students', verbose_name='Учителя', through='TeacherStudents')
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name


class TeacherStudents(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='audit')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='audit')
    audit = models.IntegerField()

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
