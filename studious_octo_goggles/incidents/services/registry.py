from __future__ import annotations

from typing import TYPE_CHECKING

from .channels.console import ConsoleChannel
from .channels.email import EmailChannel
from .channels.sms import SMSChannel

if TYPE_CHECKING:
    from .base import BaseChannel

CHANNEL_REGISTRY: dict[str, type[BaseChannel]] = {
    "console": ConsoleChannel,
    "email": EmailChannel,
    "sms": SMSChannel,
}
