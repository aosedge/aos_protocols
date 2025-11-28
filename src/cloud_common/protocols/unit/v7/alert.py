#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal, Union, Optional

from pydantic import BaseModel, Discriminator, Field, UUID4

from cloud_common.protocols.unit.constants import DataSizes
from cloud_common.protocols.unit.types import (
    TypeAlertMessageMandatory,
    TypeCoreComponentIdMandatory,
    TypeDeviceMandatory,
    TypeVersionMandatory,
)
from .common import AosIdentity, TypeItemMandatory, AosBaseModel
from ..common import TypeAosErrorInfoOptional


class AosBaseAlert(BaseModel):
    timestamp: Annotated[
        datetime,
        Field(
            alias='timestamp',
            description='Timestamp when alert was triggered in ISO8601 format.',
        ),
    ]


class AosAlertSystemErrorV7(AosBaseAlert):
    """Aos Unit system error alert information."""

    tag: Annotated[
        Literal['systemAlert'],
        Field(description='Type of the alert.'),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='Node ID of the alert.',
        ),
    ]

    message: TypeAlertMessageMandatory


class AosAlertCoreV7(AosBaseAlert):
    """Aos Unit core alert information."""

    tag: Annotated[
        Literal['coreAlert'],
        Field(description='Type of the alert.'),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='Node identification of the alert.',
        ),
    ]

    core_component: TypeCoreComponentIdMandatory
    message: TypeAlertMessageMandatory


class AosAlertResourceAllocateV7(AosBaseAlert):
    """Aos Unit device allocation alert information."""

    tag: Annotated[
        Literal['deviceAllocateAlert'],
        Field(description='Type of the alert.'),
    ]

    item: TypeItemMandatory

    subject: Annotated[
        AosIdentity,
        Field(
            alias='subject',
            description='Subject unique identifier.',
        ),
    ]

    instance: Annotated[
        int,
        Field(
            description='Service instance number (starting from 0).',
        ),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='Node ID where the alert occurs.',
        ),
    ]

    resource: TypeDeviceMandatory
    message: TypeAlertMessageMandatory


class AosAlertSystemQuotaV7(AosBaseAlert):
    """Aos Unit system quota alert information."""

    tag: Annotated[
        Literal['systemQuotaAlert'],
        Field(description='Type of the alert.'),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='Node ID of the alert.',
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


class AosAlertInstanceQuotaV7(AosBaseAlert):
    """Aos Unit instance quota alert information."""

    tag: Annotated[
        Literal['instanceQuotaAlert'],
        Field(description='Type of the alert.'),
    ]

    item: TypeItemMandatory

    subject: Annotated[
        AosIdentity,
        Field(
            alias='subject',
            description='Subject unique identifier.',
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



class AosAlertDownloadProgressV7(AosBaseAlert):
    """Aos Unit downloads alert information."""

    tag: Annotated[
        Literal['downloadProgressAlert'],
        Field(description='Type of the alert.'),
    ]

    digest: Annotated[
        str,
        Field(
            alias='digest',
            decription='Digest from AosUpdateItemBlobInfo.digest',
        ),
    ]

    url: Annotated[
        Optional[str],
        Field(
            alias='url',
            default=None,
            description='URL of the file.',
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

    state: Annotated[
        Literal[
            'started',
            'paused',
            'interrupted',
            'finished',
        ],
        Field(
            description='State of the download.',
        ),
    ]

    reason: Annotated[
        Optional[str],
        Field(
            default=None,
            description='Reason of the download state.',
        ),
    ] = None

    error_info: TypeAosErrorInfoOptional


class AosAlertUpdateItemInstanceV7(AosBaseAlert):
    """Aos Unit service instance alert information."""

    tag: Annotated[
        Literal['updateItemInstanceAlert'],
        Field(description='Type of the alert.'),
    ]

    item: TypeItemMandatory

    subject: Annotated[
        AosIdentity,
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


class AosAlertsV7(AosBaseModel):
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
                    AosAlertCoreV7,
                    AosAlertResourceAllocateV7,
                    AosAlertDownloadProgressV7,
                    AosAlertInstanceQuotaV7,
                    AosAlertUpdateItemInstanceV7,
                    AosAlertSystemErrorV7,
                    AosAlertSystemQuotaV7,
                ],
                Discriminator('tag'),
            ]
        ],
        Field(
            description='List of AosEdge alert items.',
        ),
    ]
