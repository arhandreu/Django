import random

import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def url():
    return '/api/v1/courses/'


@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture()
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, url, course_factory):
    """  Retrieve-логика """
    courses = course_factory(_quantity=20)
    course = random.choice(courses)
    response = client.get(url + f'{course.id}/')
    assert response.status_code == 200
    assert course.id == response. json()['id']


@pytest.mark.django_db
def test_get_courses(client, url, course_factory):
    """ List-логика """
    courses = course_factory(_quantity=20)
    response = client.get(url)
    assert response.status_code == 200
    for i, c in enumerate(response.json()):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id_courses(client, url, course_factory):
    """ Фильтрация по id """
    courses = course_factory(_quantity=20)
    id = random.choice(courses).id
    response = client.get(url, {'id': id})
    assert response.status_code == 200
    assert len(response.json()) == 1


@pytest.mark.django_db
def test_filter_name_courses(client, url, course_factory, student_factory):
    """ Фильтрация по name """
    students = student_factory(_quantity=100)
    courses = course_factory(_quantity=20, students=random.choices(students, k=20))
    name = random.choice(courses).name
    count = Course.objects.filter(name=name).count()
    response = client.get(url, {'name': name})
    assert response.status_code == 200
    assert len(response.json()) == count


data_create = [({'name': 'Python'}, 201), ({'name': 'Java', 'students': [1, 2, 3]}, 400)]
data_update = [({'name': 'Python'}, 200), ({'name': 'Java', 'students': [1, 2, 3]}, 400)]


@pytest.mark.django_db
@pytest.mark.parametrize('a, b', data_create)
def test_create_course(client, url, a, b):
    """ Создание курса """
    response = client.post(url, data=a)
    assert response.status_code == b


@pytest.mark.django_db
@pytest.mark.parametrize('a, b', data_update)
def test_update_course(client, url, course_factory, a, b):
    """  Обновление курса  """
    courses = course_factory(_quantity=20,)
    course = random.choice(courses)
    response = client.patch(url + f'{course.id}/', data=a)
    assert response.status_code == b
    if b == 200:
        assert course.id == response. json()['id']


@pytest.mark.django_db
def test_delete_course(client, url, course_factory):
    """  Удаление курса  """
    courses = course_factory(_quantity=20)
    course = random.choice(courses)
    response = client.delete(url + f'{course.id}/')
    assert response.status_code == 204


# @pytest.mark.django_db
# def test_count_students(settings):
#     assert settings.MAX_STUDENTS_PER_COURSE == False
