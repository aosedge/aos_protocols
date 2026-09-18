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
            default='30s',
            description="""\
Interval between resource usage samples. Default: 30s.
Format: duration string (e.g. "30s", "1m", "5m").""",
            examples=['30s', '1m', '5m'],
        ),
    ]

    average_window: Annotated[
        Optional[str],
        Field(
            alias='averageWindow',
            default='90s',
            description="""\
Sliding window for computing resource usage averages. Default: 90s.
Format: duration string (e.g. "90s", "5m", "10m").""",
            examples=['90s', '5m', '10m'],
        ),
    ]
