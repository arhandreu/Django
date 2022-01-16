from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters


from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = filters.DateTimeFromToRangeFilter()
    creator = filters.NumberFilter()
    title = filters.CharFilter()
    status = filters.CharFilter()
    favorite = filters.ModelMultipleChoiceFilter(queryset=get_user_model().objects.all())

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'title', 'status', 'favorite']
