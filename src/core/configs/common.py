#
#  Copyright (c) 2026 EPAM Systems Inc.
#
from typing import Annotated, Optional

from pydantic import BaseModel, Field


class MonitoringConfig(BaseModel):
    """Node monitoring subsystem configuration."""

    poll_period: Annotated[
        Optional[str],
        Field(
            alias='pollPeriod',
            default='35s',
            description="""\
Interval between resource usage samples. Default: 35s.
Format: duration string (e.g. "35s", "1m", "5m").""",
            examples=['35s', '1m', '5m'],
        ),
    ]

    average_window: Annotated[
        Optional[str],
        Field(
            alias='averageWindow',
            default='35s',
            description="""\
Sliding window for computing resource usage averages. Default: 35s.
Format: duration string (e.g. "35s", "5m", "10m").""",
            examples=['35s', '5m', '10m'],
        ),
    ]
