#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal, Optional

from pydantic import BaseModel, Field, field_serializer

from cloud_common.protocols.unit.common import TypeAosErrorInfoOptional
from cloud_common.protocols.unit.constants import DataSizes
from cloud_common.protocols.unit.types import (
    TypeInstanceNoOptional,
)
from .common import AosIdentity, TypeItemMandatory, TypeItemOptional, AosBaseModel
from .types import TypeInstanceNoMandatory


class AosEnvVarStatus(BaseModel):
    """The current status of the environment variable."""

    name: Annotated[
        str,
        Field(
            alias='name',
            title='Name',
            description='The unique identifier (name) of the variable.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional


class AosEnvVarInstanceStatusV7(BaseModel):
    """The current status of the environment variable."""

    item: TypeItemMandatory

    subject: Annotated[
        AosIdentity,
        Field(
            alias='subjectId',
            description='The identification of the subject.',
        ),
    ]

    instance: TypeInstanceNoMandatory

    name: Annotated[
        str,
        Field(
            alias='name',
            title='Name',
            description='The unique identifier (name) of the variable.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional


class AosEnvVar(BaseModel):

    name: Annotated[
        str,
        Field(
            alias='name',
            title='Name',
            min_length=1,
            max_length=DataSizes.DATA_LENGTH_256,
            description='The name of the environment variable.',
            examples=['PATH', '_TMP'],
        ),
    ]

    value: Annotated[  # noqa: WPS110
        str,
        Field(
            alias='value',
            title='Value',
            min_length=0,
            max_length=DataSizes.DATA_LENGTH_10240,
            description='The value of the environment variable.',
            examples=['', '/tmp'],  # noqa: S108
        ),
    ]

    ttl: Annotated[
        datetime,
        Field(
            default=None,
            title='TTL',
            description='Time to live of the variable in form `HH:MM[:SS]`. Optional. Empty or 0 means forever.',
        ),
    ]

    @field_serializer('ttl')
    def serialize_ttl(self, ttl: datetime, info):  # noqa: WPS110
        return ttl.isoformat()


class AosEnvVarV7(BaseModel):
    """The current status of the environment variable."""

    item: TypeItemOptional

    subject: Annotated[
        Optional[AosIdentity],
        Field(
            default=None,
            alias='subject',
        ),
    ]

    instance: TypeInstanceNoOptional

    variables: Annotated[
        list[AosEnvVar],
        Field(
            title='Variables',
            description='The list of environment variables.',
        ),
    ]


class AosOverrideEnvVarsRequestV7(AosBaseModel):
    """
    AosUnit protocol: 'overrideEnvVars' message.

    Cloud requests EnvVar changes using this message.
    """

    message_type: Annotated[
        Literal['overrideEnvVars'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    items: Annotated[  # noqa: WPS110
        list[AosEnvVarV7],
        Field(
            title='List of filters and variables',
            description='The list of filters and environment variables to apply.',
        ),
    ]


class AosOverrideEnvVarsStatusesV7(AosBaseModel):
    """
    AosUnit protocol: 'overrideEnvVarsStatus' message.

    Unit reports EnvVar changes using this message.
    """

    message_type: Annotated[
        Literal['overrideEnvVarsStatus'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    statuses: Annotated[
        list[AosEnvVarInstanceStatusV7],
        Field(
            alias='statuses',
            title='Statuses list',
            description='The list of environment variables and their statuses.',
        ),
    ]
