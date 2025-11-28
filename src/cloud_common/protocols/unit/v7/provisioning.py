#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.common import TypeAosErrorInfoOptional
from cloud_common.protocols.unit.v7.common import AosIdentity, AosBaseModel


class AosCSR(BaseModel):
    """Aos Certificate Sign Request."""

    csr_type: Annotated[
        str,
        Field(
            alias='type',
            description='Type of the CSR',
            examples=['online', 'offline'],
        )
    ]

    csr: Annotated[
        str,
        Field(
            alias='csr',
            description='CSR in the PEM format',
        ),
    ]


class AosStartProvisioningRequestV7(AosBaseModel):
    """
    AosUnit protocol: 'startProvisioningRequest' message.

    Cloud begins provisioning process with this message
    """

    message_type: Annotated[
        Literal['startProvisioningRequest'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='The identification of the node.',
        ),
    ]

    password: Annotated[
        str,
        Field(
            alias='password',
            description='Admin (secure officer) password for the node TPM.',
        ),
    ]


class AosStartProvisioningResponseV7(AosBaseModel):
    """
    AosUnit protocol: 'startProvisioningResponse' message.
    """

    message_type: Annotated[
        Literal['startProvisioningResponse'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='The identification of the node.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional

    csrs: Annotated[
        list[AosCSR],
        Field(
            alias='csrs',
            description='List of the CSRs.',
        )
    ]


class AosIssuedCertificateV7(BaseModel):
    """Aos issued certificate."""

    certificate_type: Annotated[
        str,
        Field(
            alias='type',
            description='Type of the CSR',
            examples=['online', 'offline'],
        )
    ]

    certificate_chain: Annotated[
        str,
        Field(
            alias='chain',
            title='Chain of certificates',
            description='Chain of certificates.',
        ),
    ]


class AosFinishProvisioningRequestV7(AosBaseModel):
    """
    AosUnit protocol: 'finishProvisioningRequest' message.

    Cloud begins provisioning process with this message
    """

    message_type: Annotated[
        Literal['finishProvisioningRequest'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='The identification of the naode.',
        ),
    ]

    certificates: Annotated[
        list[AosIssuedCertificateV7],
        Field(
            alias='certificates',
            description='The list of issued certificates',
        ),
    ]

    password: Annotated[
        str,
        Field(
            alias='password',
            description='Admin (secure officer) password for the node TPM.',
        ),
    ]


class AosFinishProvisioningResponseV7(AosBaseModel):
    """
    AosUnit protocol: 'finishProvisioningResponse' message.
    """

    message_type: Annotated[
        Literal['finishProvisioningResponse'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='The identification of the node.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional


class AosDeProvisioningRequestV7(AosBaseModel):
    """
    AosUnit protocol: 'deprovisioningRequest' message.
    """

    message_type: Annotated[
        Literal['deprovisioningRequest'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='The identification of the node.',
        ),
    ]

    password: Annotated[
        str,
        Field(
            alias='password',
            description='Admin (secure officer) password for the node TPM.',
        ),
    ]


class AosDeProvisioningResponseV7(AosBaseModel):
    """
    AosUnit protocol: 'deprovisioningResponse' message.
    """

    message_type: Annotated[
        Literal['deprovisioningResponse'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='The identification of the node.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional
