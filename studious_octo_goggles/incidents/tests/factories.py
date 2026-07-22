from __future__ import annotations

from factory import Faker
from factory.django import DjangoModelFactory

from studious_octo_goggles.incidents.models import IncidentReport


class IncidentReportFactory(DjangoModelFactory[IncidentReport]):
    title = Faker("sentence", nb_words=4)
    description = Faker("paragraph")
    severity = "high"
    service_name = Faker("word")
    status = "open"
    channels = ["console", "email"]

    class Meta:
        model = IncidentReport
