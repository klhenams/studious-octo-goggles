from __future__ import annotations

import logging
from typing import Any

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


@shared_task
def send_incident_email_task(
    incident_id: int,
    recipient_list: list[str],
    message: dict[str, str],
) -> dict[str, Any]:
    subject = message.get("subject", f"[Incident Alert] {incident_id}")
    body = message.get("body", "")

    sender = getattr(settings, "DEFAULT_FROM_EMAIL", None) or getattr(
        settings,
        "SERVER_EMAIL",
        None,
    )

    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=sender,
            recipient_list=recipient_list,
            fail_silently=False,
        )
    except Exception:
        logger.exception(
            "Failed to send incident email alert for incident %s",
            incident_id,
        )
        return {
            "status": "failed",
            "message": "email notification failed",
            "incident_id": incident_id,
        }

    return {
        "status": "sent",
        "message": "email notification sent",
        "incident_id": incident_id,
    }
