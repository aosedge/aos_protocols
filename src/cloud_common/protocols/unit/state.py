#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.constants import DataSizes
from cloud_common.protocols.unit.types import (
    TypeInstanceNoMandatory,
    TypeServiceServiceIdMandatory,
    TypeSubjectSubjectIdMandatory,
)


class AosNewState(BaseModel):
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

    service_id: TypeServiceServiceIdMandatory
    subject_id: TypeSubjectSubjectIdMandatory
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


class AosUpdateState(AosNewState):
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


class AosStateAcceptance(BaseModel):
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

    service_id: TypeServiceServiceIdMandatory
    subject_id: TypeSubjectSubjectIdMandatory
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


class AosStateRequest(BaseModel):
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

    service_id: TypeServiceServiceIdMandatory
    subject_id: TypeSubjectSubjectIdMandatory
    instance: TypeInstanceNoMandatory

    default: Annotated[
        bool,
        Field(
            alias='default',
            title='Is default?',
            description='Is requested state is the default state?',
        ),
    ]
