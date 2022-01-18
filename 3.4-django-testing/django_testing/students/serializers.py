from itertools import count

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):

        if self.context["request"].method == 'POST':
            if count(data.get('students', [])) > 20:
                raise ValidationError("На курсе не может быть больше 20 студентов")
        if self.context["request"].method in ['PUT', 'PATCH']:
            if Course.objects.get(id=self.instance.id).students.count() + count(data.get('students', [])) > 20:
                raise ValidationError("На курсе не может быть больше 20 студентов")
        return
