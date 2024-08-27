#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from datetime import timedelta
from typing import Annotated, Optional

from pydantic import BaseModel, Field


class UnitDevice(BaseModel):
    """Schema for the `device` info structure."""

    name: Annotated[
        str,
        Field(
            alias='name',
            description="The name of the systems device.",
            examples=['camera0', 'mic0'],
        ),
    ]

    permissions: Annotated[
        str,
        Field(
            alias='permissions',
            description='The needed access permissions for the device.',
            examples=['r', 'rw', 'w'],
        ),
    ]


class RunParameters(BaseModel):
    """Schema for startup parameters."""

    start_interval: Annotated[
        Optional[timedelta],
        Field(
            alias='startInterval',
            default=None,
            description='The duration in ISO8601 format to wait service start.',
            examples=['PT10S', 'PT1M'],
        ),
    ]

    start_burst: Annotated[
        Optional[int],
        Field(
            alias='startBurst',
            default=None,
            description="""\
Service which are started more than burst times within an interval time span are not permitted to start any more.
Use `startInterval` to configure the checking interval and `startBurst`
to configure how many starts per interval are allowed.""",
            examples=[3, 10],
        ),
    ]

    restart_interval: Annotated[
        Optional[timedelta],
        Field(
            alias='restartInterval',
            default=None,
            description='The duration in ISO8601 format to wait before service restart.',
            examples=['PT1S', 'PT1M'],
        ),
    ]


class ResourceRatios(BaseModel):
    """
    Schema for resource ratios.

    Each of specified resource ratio is treated as `requested` value.
    """

    cpu: Annotated[
        Optional[float],
        Field(
            alias='cpu',
            default=None,
            description='CPU requested ratio in percents (against cpuLimit)',
        ),
    ]

    ram: Annotated[
        Optional[float],
        Field(
            alias='ram',
            default=None,
            description='RAM requested ratio in percents (against ramLimit)',
        ),
    ]

    storage: Annotated[
        Optional[float],
        Field(
            alias='storage',
            default=None,
            description='Storage requested ratio in percents (against storageLimit)',
        ),
    ]


class ServiceQuotas(BaseModel):
    """Schema for possible quotas for a service."""

    cpu_limit: Annotated[
        Optional[int],
        Field(
            alias='cpuLimit',
            default=None,
            description='CPU limit in percents',
        ),
    ]
    cpu_dmips_limit: Annotated[
        Optional[int],
        Field(
            alias='cpuDmipsLimit',
            default=None,
            description='CPU limit in DMIPs',
        ),
    ]

    ram_limit: Annotated[
        Optional[int],
        Field(
            alias='ramLimit',
            default=None,
            description='RAM limit in bytes',
        ),
    ]

    storage_limit: Annotated[
        Optional[int],
        Field(
            alias='storageLimit',
            default=None,
            description='Storage limit in bytes',
        ),
    ]

    state_limit: Annotated[
        Optional[int],
        Field(
            alias='stateLimit',
            default=None,
            description='State limit in bytes',
        ),
    ]

    tmp_limit: Annotated[
        Optional[int],
        Field(
            alias='tmpLimit',
            default=None,
            description='Temporary storage limit in bytes',
        ),
    ]

    upload_speed: Annotated[
        Optional[int],
        Field(
            alias='uploadSpeed',
            default=None,
            description='Upload limit in bytes per second',
        ),
    ]

    download_speed: Annotated[
        Optional[int],
        Field(
            alias='downloadSpeed',
            default=None,
            description='Upload limit in bytes per second',
        ),
    ]

    files_limit: Annotated[
        Optional[int],
        Field(
            alias='noFileLimit',
            default=None,
            description='Limit of opened files',
        ),
    ]

    pids_limit: Annotated[
        Optional[int],
        Field(
            alias='pidsLimit',
            default=None,
            description='Limit of PIDs',
        ),
    ]


class AlertRulePoints(BaseModel):
    """Schema alert triggering procedure."""

    min_timeout: Annotated[
        Optional[timedelta],
        Field(
            alias='minTimeout',
            description='The duration in ISO8601 for a time window to check alert rule.',
            examples=['PT10S', 'PT1M'],
        ),
    ]

    min_threshold: Annotated[
        Optional[int],
        Field(
            alias='minThreshold',
            description='The minimum threshold to stop alert.',
        ),
    ]

    max_threshold: Annotated[
        Optional[int],
        Field(
            alias='maxThreshold',
            description='The maximum threshold value to start alert.',
        ),
    ]


class AlertRulePercents(BaseModel):
    """Schema alert triggering procedure in percents."""

    min_timeout: Annotated[
        Optional[timedelta],
        Field(
            alias='minTimeout',
            description='The duration in ISO8601 for a time window to check alert rule.',
            examples=['PT10S', 'PT1M'],
        ),
    ]

    min_threshold: Annotated[
        Optional[float],
        Field(
            alias='minThreshold',
            ge=0,
            le=100,
            description='The minimum threshold to stop alert.',
        ),
    ]

    max_threshold: Annotated[
        Optional[float],
        Field(
            alias='maxThreshold',
            ge=0,
            le=100,
            description='The maximum threshold value to start alert.',
        ),
    ]


class AlertRules(BaseModel):
    """Schema for all possible alert rules."""

    ram: Annotated[
        Optional[AlertRulePercents],
        Field(
            alias='ram',
            default=None,
            description='RAM alert settings.',
        ),
    ]

    cpu: Annotated[
        Optional[AlertRulePercents],
        Field(
            alias='cpu',
            default=None,
            description='CPU alert settings.',
        ),
    ]

    storage: Annotated[
        Optional[AlertRulePercents],
        Field(
            alias='storage',
            default=None,
            description='Storage alert settings.',
        ),
    ]

    upload: Annotated[
        Optional[AlertRulePoints],
        Field(
            alias='upload',
            default=None,
            description='Upload alert settings.',
        ),
    ]

    download: Annotated[
        Optional[AlertRulePoints],
        Field(
            alias='download',
            default=None,
            description='Download alert settings.',
        ),
    ]
