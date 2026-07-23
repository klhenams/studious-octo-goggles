from django.contrib import admin

from .models import IncidentReport


@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ["title", "service_name", "severity", "status", "created_at"]
    list_filter = ["severity", "status", "created_at"]
    search_fields = ["title", "service_name", "description"]
