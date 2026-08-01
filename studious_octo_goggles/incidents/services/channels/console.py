from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from typing import Any

from studious_octo_goggles.incidents.services.base import BaseChannel

if TYPE_CHECKING:
    from studious_octo_goggles.incidents.models import IncidentReport

logger = logging.getLogger(__name__)


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
