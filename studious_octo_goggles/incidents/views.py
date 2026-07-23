from __future__ import annotations

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import IncidentReport
from .serializers import IncidentReportSerializer
from .services import broadcast_incident


class IncidentReportViewSet(viewsets.ModelViewSet):
    queryset = IncidentReport.objects.all()
    serializer_class = IncidentReportSerializer

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=["post"])
    def broadcast(self, request, pk=None):
        incident = self.get_object()
        results = broadcast_incident(incident)
        incident.broadcast_results = results
        incident.save(update_fields=["broadcast_results", "updated_at"])
        serializer = self.get_serializer(incident)
        return Response(serializer.data, status=status.HTTP_200_OK)
