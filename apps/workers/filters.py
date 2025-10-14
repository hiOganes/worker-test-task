import django_filters
from .models import Worker

class WorkerFilter(django_filters.FilterSet):
    is_active = django_filters.BooleanFilter()
    position = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Worker
        fields = ['is_active', 'position']