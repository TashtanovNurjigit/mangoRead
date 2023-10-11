from django_filters import rest_framework as filters

from manga.models import Manga


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MangaFilter(filters.FilterSet):
    genres = CharFilterInFilter(field_name='genre__name', lookup_expr='in')

    class Meta:
        model = Manga
        fields = ['genres']
