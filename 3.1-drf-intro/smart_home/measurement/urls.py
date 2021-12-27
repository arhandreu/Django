from django.urls import path
from .views import SensorsView, SensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view(), name='сенсоры'),
    path('sensors/<pk>/', SensorView.as_view(), name='сенсор'),
    path('measurements/', MeasurementView.as_view(), name='показания'),
    # TODO: зарегистрируйте необходимые маршруты
]
