from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at')

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        open_adv = Advertisement.objects.filter(creator=self.context["request"].user,
                                                status__in=["OPEN", "Открыто"]).count()
        if self.context["request"].method == 'POST':
            if open_adv >= 10 and data.get('status', "OPEN") in ["OPEN", "Открыто"]:
                raise ValidationError("Вы не можете иметь больше 10 открытых объявлений")
        if self.context["request"].method in ['PUT', 'PATCH']:
            if open_adv >= -0 and self.instance.status in ["CLOSED", "Закрыто"]:
                if data.get('status') in ["OPEN", "Открыто"]:
                    raise ValidationError("Вы не можете иметь больше 10 открытых объявлений")

        return data
