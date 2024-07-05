#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal, Union

from pydantic import BaseModel, Discriminator, Field

from cloud_common.protocols.unit.common import AosErrorInfo
from cloud_common.protocols.unit.constants import DataSizes
from cloud_common.protocols.unit.types import (
    TypeAlertMessageMandatory,
    TypeCoreComponentIdMandatory,
    TypeDeviceMandatory,
    TypeNodeIdMandatory,
    TypeVersionMandatory,
)


class AosBaseAlert(BaseModel):
    timestamp: Annotated[
        datetime,
        Field(
            alias='timestamp',
            description='Timestamp when alert was triggered in ISO8601 format.',
        ),
    ]


class AosAlertSystemError(AosBaseAlert):
    """Aos Unit system error alert information."""

    tag: Annotated[
        Literal['systemAlert'],
        Field(description='Type of the alert.'),
    ]

    node_id: TypeNodeIdMandatory
    message: TypeAlertMessageMandatory


class AosAlertCore(AosBaseAlert):
    """Aos Unit core alert information."""

    tag: Annotated[
        Literal['coreAlert'],
        Field(description='Type of the alert.'),
    ]

    node_id: TypeNodeIdMandatory
    core_component: TypeCoreComponentIdMandatory
    message: TypeAlertMessageMandatory


class AosAlertResourceValidate(AosBaseAlert):
    """Aos Unit resource validation alert information."""

    tag: Annotated[
        Literal['resourceValidateAlert'],
        Field(description='Type of the alert.'),
    ]

    node_id: TypeNodeIdMandatory

    name: Annotated[
        str,
        Field(
            alias='name',
            description='Name of the resource.',
        ),
    ]

    errors: Annotated[
        list[AosErrorInfo],
        Field(
            alias='errors',
            description='The list of caught errors',
        ),
    ]


class AosAlertDeviceAllocate(AosBaseAlert):
    """Aos Unit device allocation alert information."""

    tag: Annotated[
        Literal['deviceAllocateAlert'],
        Field(description='Type of the alert.'),
    ]

    service_id: Annotated[
        str,
        Field(
            alias='serviceId',
            description='Service unique identifier in form: UUID4.',
            min_length=1,
        ),
    ]

    subject_id: Annotated[
        str,
        Field(
            alias='subjectId',
            description='Subject unique identifier.',
            min_length=1,
        ),
    ]

    instance: Annotated[
        int,
        Field(
            description='Service instance number (starting from 0).',
        ),
    ]

    node_id: TypeNodeIdMandatory
    device: TypeDeviceMandatory
    message: TypeAlertMessageMandatory


class AosAlertSystemQuota(AosBaseAlert):
    """Aos Unit system quota alert information."""

    tag: Annotated[
        Literal['systemQuotaAlert'],
        Field(description='Type of the alert.'),
    ]

    node_id: TypeNodeIdMandatory

    parameter: Annotated[
        str,
        Field(
            description='Parameter name of the system quota.',
            min_length=1,
            max_length=DataSizes.MIDDLE_CHAR_FIELD_LENGTH,
        ),
    ]

    value: Annotated[  # noqa: WPS110
        int,
        Field(
            ge=0,
            description='Triggered value of the parameter.',
        ),
    ]


class AosAlertInstanceQuota(AosBaseAlert):
    """Aos Unit instance quota alert information."""

    tag: Annotated[
        Literal['instanceQuotaAlert'],
        Field(description='Type of the alert.'),
    ]

    service_id: Annotated[
        str,
        Field(
            alias='serviceId',
            description='Service unique identifier.',
            min_length=1,
        ),
    ]

    subject_id: Annotated[
        str,
        Field(
            alias='subjectId',
            description='Subject unique identifier.',
            min_length=1,
        ),
    ]

    instance: Annotated[
        int,
        Field(
            description='Instance number (starting from 0).',
        ),
    ]

    parameter: Annotated[
        str,
        Field(
            description='Parameter name of the system quota.',
            min_length=1,
            max_length=DataSizes.MIDDLE_CHAR_FIELD_LENGTH,
        ),
    ]

    value: Annotated[  # noqa: WPS110
        int,
        Field(
            ge=0,
            description='Triggered value of the parameter.',
        ),
    ]


class AosAlertDownloadProgress(AosBaseAlert):
    """Aos Unit download alert information."""

    tag: Annotated[
        Literal['downloadProgressAlert'],
        Field(description='Type of the alert.'),
    ]

    target_type: Annotated[
        Literal['component', 'layer', 'service'],
        Field(
            alias='targetType',
            decription='Target type of the file.',
        ),
    ]

    target_id: Annotated[
        str,
        Field(
            alias='targetId',
            decription='Target ID of the file.',
        ),
    ]

    version: TypeVersionMandatory
    message: TypeAlertMessageMandatory

    url: Annotated[
        str,
        Field(
            description='URL of the downloading file.',
        ),
    ]

    downloaded_bytes: Annotated[
        int,
        Field(
            ge=0,
            alias='downloadedBytes',
            description='Downloaded bytes at the specified moment.',
        ),
    ]

    total_bytes: Annotated[
        int,
        Field(
            ge=0,
            alias='totalBytes',
            description='Total size in bytes of the file.',
        ),
    ]


class AosAlertServiceInstance(AosBaseAlert):
    """Aos Unit service instance alert information."""

    tag: Annotated[
        Literal['serviceInstanceAlert'],
        Field(
            Field(description='Type of the alert.'),
        ),
    ]

    service_id: Annotated[
        str,
        Field(
            alias='serviceId',
            description='Service unique identifier.',
            min_length=1,
        ),
    ]

    subject_id: Annotated[
        str,
        Field(
            alias='subjectId',
            description='Subject unique identifier.',
            min_length=1,
        ),
    ]

    instance: Annotated[
        int,
        Field(
            description='Instance number (starting from 0).',
        ),
    ]

    version: TypeVersionMandatory
    message: TypeAlertMessageMandatory


class AosAlerts(BaseModel):
    message_type: Annotated[
        Literal['alerts'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]
    items: Annotated[  # noqa: WPS110
        list[
            Annotated[
                Union[
                    AosAlertCore,
                    AosAlertDeviceAllocate,
                    AosAlertDownloadProgress,
                    AosAlertInstanceQuota,
                    AosAlertServiceInstance,
                    AosAlertSystemError,
                    AosAlertSystemQuota,
                    AosAlertResourceValidate,
                ],
                Discriminator('tag'),
            ]
        ],
        Field(
            description='List of AosEdge alert items.',
        ),
    ]
