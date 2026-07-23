from __future__ import annotations

from django.urls import resolve
from django.urls import reverse


def test_incident_list() -> None:
    assert reverse("api:incidentreport-list") == "/api/incidents/"
    assert resolve("/api/incidents/").view_name == "api:incidentreport-list"


def test_incident_detail() -> None:
    assert reverse("api:incidentreport-detail", kwargs={"pk": 1}) == "/api/incidents/1/"
    assert resolve("/api/incidents/1/").view_name == "api:incidentreport-detail"


def test_incident_broadcast() -> None:
    assert (
        reverse("api:incidentreport-broadcast", kwargs={"pk": 1})
        == "/api/incidents/1/broadcast/"
    )
    assert (
        resolve("/api/incidents/1/broadcast/").view_name
        == "api:incidentreport-broadcast"
    )
