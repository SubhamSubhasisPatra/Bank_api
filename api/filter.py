import django_filters
from .models import Branches, Banks


class BranchFilter(django_filters.FilterSet):
    # band_name_filter = django_filters.NumberFilter(id='bank_id_id')

    class Meta:
        model = Branches
        fields = ['ifsc', 'city', 'bank_id']

