from __future__ import annotations

import pytest

from studious_octo_goggles.incidents.models import IncidentReport

pytestmark = pytest.mark.django_db


def test_incident_report_defaults() -> None:
    incident = IncidentReport.objects.create(
        title="Auth service outage",
        description="The authentication service is returning 502s.",
        severity="high",
        service_name="auth-service",
        channels=["console", "email"],
    )

    assert incident.status == "open"
    assert incident.channels == ["console", "email"]
    assert str(incident) == "Auth service outage"
