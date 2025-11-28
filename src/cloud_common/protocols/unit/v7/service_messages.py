#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Literal

from pydantic import Field

from .common import AosBaseModel


class AosAckV7(AosBaseModel):
    message_type: Annotated[
        Literal['ack'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]


class AosNackV7(AosBaseModel):
    message_type: Annotated[
        Literal['nack'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    retry_after: Annotated[
        int,
        Field(
            default=500,
            alias='retryAfter',
            description='Retry after time in milliseconds.',
        )
    ]
