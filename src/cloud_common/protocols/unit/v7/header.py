#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.types import TypeAosSystemIdMandatory


class AosUnitHeaderV7(BaseModel):
    """Aos Unit message header."""

    version: Annotated[
        Literal[7],
        Field(
            title='Protocol version',
            description='The version of Unit-Cloud protocol.',
        ),
    ]
    system_id: TypeAosSystemIdMandatory

    correlation_id: str = Field(
        alias='correlationId',
        default=None,
        description='Correlation ID of the request.',
    )
