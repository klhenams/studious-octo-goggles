from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from typing import Any

if TYPE_CHECKING:
    from .models import IncidentReport


logger = logging.getLogger(__name__)


class BaseChannel:
    name = "base"

    def send(self, incident: IncidentReport) -> dict[str, Any]:
        return {"channel": self.name, "status": "queued"}


class ConsoleChannel(BaseChannel):
    name = "console"

    def send(self, incident: IncidentReport) -> dict[str, Any]:
        logger.info(
            "Incident %s (%s) - %s",
            incident.title,
            incident.severity,
            incident.description,
        )
        return {
            "channel": self.name,
            "status": "sent",
            "message": "logged to console",
        }


class EmailChannel(BaseChannel):
    name = "email"

    def send(self, incident: IncidentReport) -> dict[str, Any]:
        return {
            "channel": self.name,
            "status": "sent",
            "message": "email notification queued",
        }


class SMSChannel(BaseChannel):
    name = "sms"

    def send(self, incident: IncidentReport) -> dict[str, Any]:
        return {
            "channel": self.name,
            "status": "sent",
            "message": "sms notification queued",
        }


CHANNEL_REGISTRY: dict[str, type[BaseChannel]] = {
    "console": ConsoleChannel,
    "email": EmailChannel,
    "sms": SMSChannel,
}


def broadcast_incident(incident: IncidentReport) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for channel_name in incident.channels:
        channel_cls = CHANNEL_REGISTRY.get(channel_name)
        if channel_cls is None:
            results.append({"channel": channel_name, "status": "unsupported"})
            continue
        results.append(channel_cls().send(incident))
    return results
