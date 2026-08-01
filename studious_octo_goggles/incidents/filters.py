from __future__ import annotations

import django_filters
from django.db.models import Q

from .models import IncidentReport


class IncidentReportFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search", label="Search")

    # Filter for incidents created on or after a specific timestamp
    created_after = django_filters.IsoDateTimeFilter(
        field_name="created_at",
        lookup_expr="gte",
    )
    # Filter for incidents created on or before a specific timestamp
    created_before = django_filters.IsoDateTimeFilter(
        field_name="created_at",
        lookup_expr="lte",
    )

    class Meta:
        model = IncidentReport
        fields = ["search", "severity", "status", "created_after", "created_before"]

    def filter_search(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(
            Q(title__icontains=value)
            | Q(description__icontains=value)
            | Q(service_name__icontains=value),
        )
