from __future__ import annotations

from typing import Any

from rest_framework import serializers

from .models import IncidentReport
from .services import broadcast_incident


class IncidentReportSerializer(serializers.ModelSerializer[IncidentReport]):
    broadcast_results = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = IncidentReport
        fields = [
            "id",
            "title",
            "description",
            "severity",
            "service_name",
            "status",
            "channels",
            "created_at",
            "updated_at",
            "broadcast_results",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "broadcast_results"]

    def create(self, validated_data: dict[str, Any]) -> IncidentReport:
        instance = IncidentReport.objects.create(**validated_data)
        results = broadcast_incident(instance)
        instance.broadcast_results = results
        instance.save(update_fields=["broadcast_results", "updated_at"])
        return instance

    def update(
        self,
        instance: IncidentReport,
        validated_data: dict[str, Any],
    ) -> IncidentReport:
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def get_broadcast_results(self, obj: IncidentReport) -> list[dict[str, Any]]:
        return obj.broadcast_results or []
