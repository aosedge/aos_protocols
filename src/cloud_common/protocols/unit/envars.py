#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, Field, field_serializer

from cloud_common.protocols.unit.common import TypeAosErrorInfoOptional
from cloud_common.protocols.unit.constants import DataSizes
from cloud_common.protocols.unit.types import (
    TypeInstanceNoOptional,
    TypeServiceServiceIdOptional,
    TypeSubjectSubjectIdOptional,
)


class AosEnvVarStatus(BaseModel):
    """The current status of the environment variable."""

    envar_id: Annotated[
        str,
        Field(
            alias='name',
            title='Name',
            description='The unique identifier (name) of the variable.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional


class AosEnvVarInstanceStatus(BaseModel):
    """The current status of the environment variable."""

    service_id: TypeServiceServiceIdOptional
    subject_id: TypeSubjectSubjectIdOptional
    instance: TypeInstanceNoOptional

    statuses: Annotated[
        list[AosEnvVarStatus],
        Field(
            alias='statuses',
            title='Statuses list',
            description='The list of environment variables and their statuses.',
        ),
    ]


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


class AosServiceEnvVar(BaseModel):
    """The current status of the environment variable."""

    service_id: TypeServiceServiceIdOptional
    subject_id: TypeSubjectSubjectIdOptional
    instance: TypeInstanceNoOptional

    variables: Annotated[
        list[AosEnvVar],
        Field(
            title='Variables',
            description='The list of environment variables.',
        ),
    ]


class AosOverrideEnvVarsRequest(BaseModel):
    """
    AosUnit protocol: 'overrideEnvVars' message.

    Unit reports EnvVar changes using this message.
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
        list[AosServiceEnvVar],
        Field(
            title='List of filters and variables',
            description='The list of filters and environment variables to apply.',
        ),
    ]


class AosOverrideEnvVarsStatuses(BaseModel):
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
        list[AosEnvVarInstanceStatus],
        Field(
            alias='statuses',
            title='Statuses list',
            description='The list of environment variables and their statuses.',
        ),
    ]
