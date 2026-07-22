from __future__ import annotations

from rest_framework import viewsets

from .models import IncidentReport
from .serializers import IncidentReportSerializer


class IncidentReportViewSet(viewsets.ModelViewSet):
    queryset = IncidentReport.objects.all()
    serializer_class = IncidentReportSerializer

    def perform_create(self, serializer):
        serializer.save()
