from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):

    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE, verbose_name='Датчик')
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Температура')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата')
    image = models.ImageField(default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'

    def __str__(self):
        return self.sensor.name + self.created_at.strftime(" %B %d, %Y")
