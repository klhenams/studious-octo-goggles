from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

if TYPE_CHECKING:
    from studious_octo_goggles.incidents.models import IncidentReport


class BaseChannel:
    name = "base"

    def send(self, incident: IncidentReport) -> dict[str, Any]:
        return {"channel": self.name, "status": "queued"}
