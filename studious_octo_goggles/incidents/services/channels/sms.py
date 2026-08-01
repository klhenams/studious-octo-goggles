from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from studious_octo_goggles.incidents.services.base import BaseChannel

if TYPE_CHECKING:
    from studious_octo_goggles.incidents.models import IncidentReport


class SMSChannel(BaseChannel):
    name = "sms"

    def send(self, incident: IncidentReport) -> dict[str, Any]:
        return {
            "channel": self.name,
            "status": "sent",
            "message": "sms notification queued",
        }
