from .base import BaseChannel
from .channels import ConsoleChannel
from .channels import EmailChannel
from .channels import SMSChannel
from .registry import CHANNEL_REGISTRY

__all__ = [
    "CHANNEL_REGISTRY",
    "BaseChannel",
    "ConsoleChannel",
    "EmailChannel",
    "SMSChannel",
]


def broadcast_incident(incident):
    results = []
    for channel_name in incident.channels:
        channel_cls = CHANNEL_REGISTRY.get(channel_name)
        if channel_cls is None:
            results.append({"channel": channel_name, "status": "unsupported"})
            continue
        results.append(channel_cls().send(incident))
    return results
