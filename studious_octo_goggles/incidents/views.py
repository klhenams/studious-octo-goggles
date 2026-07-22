from __future__ import annotations

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import IncidentReport
from .serializers import IncidentReportSerializer


class IncidentReportViewSet(viewsets.ModelViewSet):
    queryset = IncidentReport.objects.all()
    serializer_class = IncidentReportSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()
