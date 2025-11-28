#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.constants import DataSizes
from cloud_common.protocols.unit.types import (
    TypeInstanceNoMandatory,
)
from .common import AosIdentity, TypeSubjectMandatory, TypeItemMandatory, AosBaseModel


class AosNewStateV7(AosBaseModel):
    """
    AosUnit protocol: 'newState' message.

    Unit reports service state changes using this message.
    """

    message_type: Annotated[
        Literal['newState'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    item: Annotated[
        AosIdentity,
        Field(
            default=None,
            alias='item',
            description='The identification of the resource (service).',
        ),
    ]

    subject: Annotated[
        AosIdentity,
        Field(
            default=None,
            alias='subject',
            description='The identification of the subject.',
        ),
    ]

    instance: TypeInstanceNoMandatory

    checksum: Annotated[
        str,
        Field(
            alias='stateChecksum',
            title='State checksum (digest)',
            min_length=1,
            max_length=DataSizes.DATA_LENGTH_256,
            description='The checksum (digest) over state content',
        ),
    ]

    state: Annotated[
        str,
        Field(
            alias='state',
            title='State content',
            min_length=0,
            description='The state content',
        ),
    ]


class AosUpdateStateV7(AosNewStateV7):
    """
    AosUnit protocol: 'updateState' message.

    Cloud reports service state changes using this message.
    """

    message_type: Annotated[
        Literal['updateState'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]


class AosStateAcceptanceV7(AosBaseModel):
    """
    AosUnit protocol: 'stateAcceptance' message.

    Cloud reports service state changes using this message.
    """

    message_type: Annotated[
        Literal['stateAcceptance'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    item: TypeItemMandatory
    subject: TypeSubjectMandatory
    instance: TypeInstanceNoMandatory

    checksum: Annotated[
        str,
        Field(
            alias='checksum',
            title='State checksum (digest)',
            min_length=1,
            max_length=DataSizes.DATA_LENGTH_256,
            description='The checksum (digest) over state content',
        ),
    ]

    result: Annotated[  # noqa: WPS110
        Literal['accepted', 'rejected'],
        Field(
            alias='result',
            title='Result of applying state change',
            description='The result of applying state change.',
        ),
    ]

    reason: Annotated[
        str,
        Field(
            alias='reason',
            title='Reason of applying state change',
            min_length=0,
            description='The reason of applying state change.',
        ),
    ]


class AosStateRequestV7(AosBaseModel):
    """
    AosUnit protocol: 'newState' message.

    Unit request service state.
      - if `default` field is equal to `true` - AosEdge Cloud will return the initial (default) state.
      - else AosEdge Cloud will return current state (the latest)
    """

    message_type: Annotated[
        Literal['stateRequest'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    item: TypeItemMandatory
    subject: TypeSubjectMandatory
    instance: TypeInstanceNoMandatory

    default: Annotated[
        bool,
        Field(
            alias='default',
            title='Is default?',
            description='Is requested state is the default state?',
        ),
    ]
