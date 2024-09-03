#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.types import (
    TypeInstanceNoMandatory,
    TypeNodeIdMandatory,
    TypeServiceServiceIdMandatory,
    TypeSubjectSubjectIdMandatory,
)


class AosPartitionUsage(BaseModel):
    """PartitionUsage partition usage information."""

    name: Annotated[
        str,
        Field(
            alias='name',
            description='Name of disk partition',
        ),
    ]

    used_size: Annotated[
        int,
        Field(
            alias='usedSize',
            description='Used of disk partition in bytes',
        ),
    ]


class AosMonitoringData(BaseModel):
    """AosEdge monitoring data."""

    timestamp: Annotated[
        datetime,
        Field(
            alias='timestamp',
            description='Timestamp when unit monitoring was recorded in ISO8601 format',
        ),
    ]

    ram: Annotated[
        int,
        Field(
            alias='ram',
            description='RAM Parameter of unit monitoring',
        ),
    ]

    cpu: Annotated[
        int,
        Field(
            alias='cpu',
            description='CPU Parameter of unit monitoring',
        ),
    ]

    download: Annotated[
        int,
        Field(
            default=None,
            alias='download',
            description='In Traffic Parameter of unit monitoring',
        ),
    ]

    upload: Annotated[
        int,
        Field(
            default=None,
            alias='upload',
            description='Out Traffic Parameter of unit monitoring',
        ),
    ]

    partitions: Annotated[
        list[AosPartitionUsage],
        Field(
            default=None,
            alias='partitions',
            description='Usage of disk partitions',
        ),
    ]


class AosInstanceMonitoringData(BaseModel):
    """AosEdge unit monitoring data for service."""

    service_id: TypeServiceServiceIdMandatory
    subject_id: TypeSubjectSubjectIdMandatory
    instance: TypeInstanceNoMandatory
    node_id: TypeNodeIdMandatory

    items: Annotated[  # noqa: WPS110
        list[AosMonitoringData],
        Field(
            alias='items',
            description='List of the monitoring records',
        ),
    ]


class AosNodeMonitoringData(BaseModel):
    """AosEdge unit monitoring information."""

    node_id: TypeNodeIdMandatory

    items: Annotated[  # noqa: WPS110
        list[AosMonitoringData],
        Field(
            alias='items',
            description='List of the monitoring records.',
        ),
    ]


class AosMonitoring(BaseModel):

    message_type: Annotated[
        Literal['monitoringData'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    nodes: Annotated[  # noqa: WPS110
        list[AosNodeMonitoringData],
        Field(
            description='List of AosEdge unit monitoring items',
        ),
    ]

    service_instances: Annotated[
        list[AosInstanceMonitoringData],
        Field(
            default=None,
            alias='serviceInstances',
            description='List of AosEdge unit monitoring got from services.',
        ),
    ]
