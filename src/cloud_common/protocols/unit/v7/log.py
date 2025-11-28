#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal, Optional

from pydantic import Base64Bytes, BaseModel, Field, field_serializer

from cloud_common.protocols.unit.common import TypeAosErrorInfoOptional
from cloud_common.protocols.unit.types import (
    TypeAosLogId,
    TypeInstanceNoOptional,
)
from .common import AosIdentity, TypeItemOptional, AosBaseModel


class AosLogFilterV7(BaseModel):
    """The filter options applied to logs."""

    from_timestamp: Annotated[
        datetime,
        Field(
            default=None,
            alias='from',
            title='From',
            description='Start timestamp of the logs in ISO8601 format. Applied operator: `>=`.',
        ),
    ]

    till_timestamp: Annotated[
        datetime,
        Field(
            default=None,
            alias='till',
            title='Till',
            description='End timestamp of the logs in ISO8601 format. Applied operator: `<`.',
        ),
    ]

    nodes: Annotated[
        list[AosIdentity],
        Field(
            default=None,
            alias='nodeIds',
            title='Nodes',
            description='The optional list of the Nodes to look for logs. If field ia omitted all nodes are used.',
        ),
    ]

    item: TypeItemOptional

    subject: Annotated[
        Optional[AosIdentity],
        Field(
            default=None,
            alias='subject',
            description='The identification of the resource.',
        ),
    ]

    instance: TypeInstanceNoOptional

    @field_serializer('from_timestamp')
    def serialize_from_timestamp(self, from_timestamp: datetime, info):  # noqa: WPS110
        return from_timestamp.isoformat('T', 'seconds')

    @field_serializer('till_timestamp')
    def serialize_till_timestamp(self, till_timestamp: datetime, info):  # noqa: WPS110
        return till_timestamp.isoformat('T', 'seconds')


class AosUploadLogOptions(BaseModel):
    """The description of used channel to upload logs."""

    type: Annotated[
        Literal['wss', 'https'],
        Field(
            title='Type of the channel',
            description='The channel protocol used to upload logs.',
        ),
    ]

    url: Annotated[
        Optional[str],
        Field(
            default=None,
            title='URL',
            description='The base URL used to upload.',
        ),
    ]

    bearer_token: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='bearerToken',
            title='Bearer token',
            description='The token to use in the `Authorization` header.',
        ),
    ]

    bearer_token_ttl: Annotated[
        Optional[datetime],
        Field(
            default=None,
            alias='bearerTokenTtl',
            title='Bearer token TTL',
            description='Time to live of the token in ISO8601 format.',
        ),
    ]


class AosRequestLogV7(AosBaseModel):
    """
    AosUnit protocol: 'requestLog' message.

    Cloud requests the specified logs from the Unit.
    """

    message_type: Annotated[
        Literal['requestLog'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    log_type: Annotated[
        Literal['systemLog', 'instanceLog', 'crashLog'],
        Field(
            alias='logType',
            description='The type of requested logs.',
        ),
    ]

    filter: Annotated[
        AosLogFilterV7,
        Field(
            title='Filter',
            description='The filters for the requested logs.',
        ),
    ]

    upload_options: Annotated[
        AosUploadLogOptions,
        Field(
            default=None,
            alias='uploadOptions',
            description='The upload options. The absense means use AMQPs channel.',
        ),
    ]


class AosPushLogV7(AosBaseModel):
    """
    AosUnit protocol: 'pushLog' message.

    Unit sends the specified logs to the Cloud.
    """

    message_type: Annotated[
        Literal['pushLog'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='The identification of the node.',
        ),
    ]

    part: Annotated[
        int,
        Field(
            alias='part',
            title='Part #',
            default=None,
            description='The No of the current part. Starts with 0.',
        ),
    ]

    parts_count: Annotated[
        int,
        Field(
            alias='partsCount',
            title='Parts count',
            default=None,
            description='The total count of parts.',
        ),
    ]

    content: Annotated[  # noqa: WPS110
        Base64Bytes,
        Field(
            default=None,
            title='Content',
            description='The base64 encoded content of the specified part of the log file.',
        ),
    ]

    status: Annotated[
        Literal[
            'ok',
            'failed',
            'empty',
            'absent',
        ],
        Field(
            title='Status',
            description='The log status for the specified Node.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional
