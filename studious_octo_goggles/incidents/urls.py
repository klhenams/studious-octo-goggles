from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import IncidentReportViewSet

router = DefaultRouter()
router.register(r"incidents", IncidentReportViewSet, basename="incidentreport")

urlpatterns = [
    path("", include(router.urls)),
]
