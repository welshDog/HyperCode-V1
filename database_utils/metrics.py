"""Lightweight metrics helper for writing ResearchMetrics rows."""

from typing import Any, Optional

from sqlalchemy.orm import Session

from .models import ResearchMetrics


def record_metric(
    session: Session,
    *,
    name: str,
    value: Optional[float] = None,
    data: Optional[dict[str, Any]] = None,
    agent_id: Optional[int] = None,
    task_id: Optional[int] = None,
) -> ResearchMetrics:
    """Persist a metrics record. Caller owns commit."""
    metric = ResearchMetrics(
        metric_name=name,
        metric_value=value,
        metric_data=data,
        agent_id=agent_id,
        task_id=task_id,
    )
    session.add(metric)
    return metric

