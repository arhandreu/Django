from django.contrib import admin

from .models import Student, Teacher, TeacherStudents


class TeacherStudentsInline(admin.StackedInline):
    model = TeacherStudents
    extra = 2


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [TeacherStudentsInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
