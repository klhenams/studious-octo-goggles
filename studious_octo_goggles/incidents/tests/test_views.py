from __future__ import annotations

import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from studious_octo_goggles.incidents.tests.factories import IncidentReportFactory
from studious_octo_goggles.incidents.views import IncidentReportViewSet
from studious_octo_goggles.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_incident_list_view_returns_paginated_results() -> None:
    user = UserFactory.create()
    factory = APIRequestFactory()
    request = factory.get(reverse("api:incidentreport-list"))
    force_authenticate(request, user=user)

    view = IncidentReportViewSet.as_view({"get": "list"})
    response = view(request)

    assert response.status_code == 200  # noqa: PLR2004
    assert "results" in response.data
    assert response.data["count"] == 0


def test_incident_create_view_broadcasts_channels() -> None:
    user = UserFactory.create()
    factory = APIRequestFactory()
    payload = {
        "title": "Auth service outage",
        "description": "The authentication service is returning 502s.",
        "severity": "high",
        "service_name": "auth-service",
        "channels": ["console", "email"],
    }
    request = factory.post(reverse("api:incidentreport-list"), payload, format="json")
    force_authenticate(request, user=user)

    view = IncidentReportViewSet.as_view({"post": "create"})
    response = view(request)

    assert response.status_code == 201  # noqa: PLR2004
    assert response.data["title"] == payload["title"]
    assert response.data["status"] == "open"
    assert response.data["channels"] == payload["channels"]
    assert len(response.data["broadcast_results"]) == 2  # noqa: PLR2004


def test_incident_broadcast_action_returns_results() -> None:
    user = UserFactory.create()
    incident = IncidentReportFactory.create(channels=["console", "email"])
    factory = APIRequestFactory()
    request = factory.post(
        reverse("api:incidentreport-broadcast", kwargs={"pk": incident.pk}),
    )
    force_authenticate(request, user=user)

    view = IncidentReportViewSet.as_view({"post": "broadcast"})
    response = view(request, pk=incident.pk)

    assert response.status_code == 200  # noqa: PLR2004
    assert len(response.data["broadcast_results"]) == 2  # noqa: PLR2004
