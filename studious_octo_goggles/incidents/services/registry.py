from __future__ import annotations

from typing import TYPE_CHECKING

from .channels import ConsoleChannel
from .channels import EmailChannel
from .channels import SMSChannel

if TYPE_CHECKING:
    from .base import BaseChannel

CHANNEL_REGISTRY: dict[str, type[BaseChannel]] = {
    "console": ConsoleChannel,
    "email": EmailChannel,
    "sms": SMSChannel,
}
