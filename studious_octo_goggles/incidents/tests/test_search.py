from __future__ import annotations

import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from studious_octo_goggles.incidents.tests.factories import IncidentReportFactory
from studious_octo_goggles.incidents.views import IncidentReportViewSet
from studious_octo_goggles.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_incident_list_supports_search_filter() -> None:
    UserFactory.create()
    IncidentReportFactory.create(title="API outage", service_name="api", status="open")
    IncidentReportFactory.create(
        title="Database issue",
        service_name="db",
        status="resolved",
    )

    factory = APIRequestFactory()
    request = factory.get(reverse("api:incidentreport-list"), {"search": "outage"})
    force_authenticate(request, user=UserFactory.create())

    view = IncidentReportViewSet.as_view({"get": "list"})
    response = view(request)

    assert response.status_code == 200  # noqa: PLR2004
    assert response.data["count"] == 1
    assert response.data["results"][0]["title"] == "API outage"
