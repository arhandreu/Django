from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]
        return []
