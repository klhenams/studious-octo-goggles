from __future__ import annotations

from django.db import models

from .constants import SEVERITY_CHOICES
from .constants import STATUS_CHOICES


class IncidentReport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default="medium",
    )
    service_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    channels = models.JSONField(default=list)
    broadcast_results = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
