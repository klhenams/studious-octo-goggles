from __future__ import annotations

import logging
from email.utils import getaddresses
from typing import TYPE_CHECKING
from typing import Any

from django.conf import settings

from studious_octo_goggles.incidents.services.base import BaseChannel
from studious_octo_goggles.incidents.tasks import send_incident_email_task

if TYPE_CHECKING:
    from studious_octo_goggles.incidents.models import IncidentReport

logger = logging.getLogger(__name__)


class EmailChannel(BaseChannel):
    name = "email"

    def _compose_message(self, incident: IncidentReport) -> dict[str, str]:
        subject = f"[Incident Alert] {incident.title}"
        body = (
            f"Title: {incident.title}\n"
            f"Severity: {incident.severity}\n"
            f"Service: {incident.service_name}\n"
            f"Status: {incident.status}\n\n"
            f"Description: {incident.description}"
        )
        return {"subject": subject, "body": body}

    def send(self, incident: IncidentReport) -> dict[str, Any]:
        configured_recipients = getattr(settings, "INCIDENT_ALERT_RECIPIENTS", [])
        if configured_recipients:
            recipient_list = [email for _, email in getaddresses(configured_recipients)]
        else:
            manager_recipients = [
                email for _, email in getaddresses(getattr(settings, "MANAGERS", []))
            ]
            admin_recipients = [
                email for _, email in getaddresses(getattr(settings, "ADMINS", []))
            ]
            recipient_list = manager_recipients or admin_recipients

        if not recipient_list:
            return {
                "channel": self.name,
                "status": "failed",
                "message": "no email recipients configured",
            }

        message = self._compose_message(incident)
        send_incident_email_task.delay(
            incident_id=incident.pk,
            recipient_list=recipient_list,
            message=message,
        )

        return {
            "channel": self.name,
            "status": "queued",
            "message": "email notification queued",
            "recipients": recipient_list,
        }
