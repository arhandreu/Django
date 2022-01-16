from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrStuff
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    @action(detail=True, methods=['PATCH'], permission_classes=[IsAuthenticated])
    def change_fav(self, request, pk=None):
        obj = self.get_object()
        user = request.user
        if user.is_anonymous:
            return Response({'answer': 'Вы не авторизованы'})
        if user == obj.creator:
            return Response({'answer': 'Вы автор и не можете добавить статью в избранное!'})
        else:
            if user in obj.favorite.all():
                obj.favorite.remove(user)
                return Response({'answer': 'Cтатья удалена из избранного'})
            else:
                obj.favorite.add(user)
                return Response({'answer': 'Cтатья добавлены в избранные'})

    def list(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            queryset = self.filter_queryset(Advertisement.objects.filter(Q(draft=False) | Q(creator=request.user)))
        else:
            queryset = self.filter_queryset(Advertisement.objects.filter(draft=False))
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrStuff()]
        return []

