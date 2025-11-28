#
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal, Optional, Dict

from pydantic import BaseModel, Field, field_serializer, SecretStr

from cloud_common.protocols.unit.types import (
    TypeCertificatesType,
    TypeStatusForNonExecutables,
)
from .common import AosIdentity, AosBaseModel
from ..common import TypeAosErrorInfoOptional


class AosCertificateIdentificationV7(BaseModel):
    """Certificate identification data."""

    type: TypeCertificatesType

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='The identity of the node.',
        ),
    ]


class AosCertificateIdentificationValidTillV7(AosCertificateIdentificationV7):
    """Certificate identification data with valid till."""

    serial: Annotated[
        str,
        Field(
            default=None,
            alias='serial',
            title='Serial of the Certificate',
            description='Serial of the Certificate.',
        ),
    ]

    valid_till: Annotated[
        datetime,
        Field(
            default=None,
            alias='validTill',
            title='Valid Till',
            description='The valid till of the Certificate.',
        ),
    ]

    @field_serializer('valid_till')
    def serialize_valid_till(self, valid_till: datetime, info):  # noqa: WPS110
        return valid_till.isoformat()


class AosNodeSecretV7(BaseModel):
    """Node related secret data."""

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
            description='The identity of the node.',
        ),
    ]

    secret: Annotated[
        SecretStr,
        Field(
            alias='secret',
            description='Secret value for a node.',
        ),
    ]


class AosUnitSecretsDataV7(BaseModel):
    """Keeps the unit secret used to decode secure device information."""

    version: Annotated[
        Literal[7],
        Field(
            alias='version',
            title='Version',
            description='Version of the unit secrets structure.',
        ),
    ]

    nodes: Annotated[
        Optional[AosNodeSecretV7],
        Field(
            default=None,
            description='Nodes and secrets list.',
        ),
    ]


class AosRenewCertsNotificationV7(AosBaseModel):
    """
    AosUnit protocol: 'renewCertificatesNotification' message.

    Cloud sends renew certificate notification from cloud with unit secrets.
    """

    message_type: Annotated[
        Literal['renewCertificatesNotification'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    certificates: Annotated[
        list[AosCertificateIdentificationValidTillV7],
        Field(
            alias='certificates',
            title='Certificates',
            description='The list of certificates that were renewed.',
        ),
    ]

    unit_secrets: Annotated[
        AosUnitSecretsDataV7,
        Field(
            alias='unitSecrets',
            title='Unit Secrets',
            description='The unit secrets',
            examples=[
                {
                    'version': 1,
                    'nodes': {
                        'Node0': 'mega strong secret',
                        'Node1': 'super strong secret',
                    },
                }
            ]
        ),
    ]


class AosIssuedUnitCertsV7(AosCertificateIdentificationV7):
    """IssuedUnitCerts issued unit certificates info."""

    certificate_chain: Annotated[
        str,
        Field(
            alias='certificateChain',
            title='Chain of certificates',
            description='Chain of certificates.',
        ),
    ]


class AosIssuedUnitCertificatesV7(AosBaseModel):
    """
    AosUnit protocol: 'issuedUnitCertificates' message.

    Cloud sends issued unit certificates info.
    """

    message_type: Annotated[
        Literal['issuedUnitCertificates'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    certificates: Annotated[
        list[AosIssuedUnitCertsV7],
        Field(
            alias='certificates',
            title='Certificates',
            description='The list of certificates that were issued.',
        ),
    ]


class AosIssueCertData(AosCertificateIdentificationV7):
    """IssueCertData issue certificate data."""

    csr: Annotated[
        str,
        Field(
            alias='csr',
            title='CSR',
            description='Certificate Signing Request.',
        ),
    ]


class AosIssueUnitCertificatesV7(AosBaseModel):
    """
    AosUnit protocol: 'issueUnitCertificates' message.

    Unit sends issue unit certificates request.
    """

    message_type: Annotated[
        Literal['issueUnitCertificates'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    requests: Annotated[
        list[AosIssueCertData],
        Field(
            alias='requests',
            title='Request to issue certificates',
            description='Request to issue certificates.',
        ),
    ]


class AosInstallCertDataV7(AosCertificateIdentificationV7):
    """InstallCertData install certificate data."""

    serial: Annotated[
        str,
        Field(
            alias='serial',
            title='Serial of the Certificate',
            description='Serial of the Certificate.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional


class AosInstallUnitCertificatesConfirmationV7(AosBaseModel):
    """
    AosUnit protocol: 'installUnitCertificatesConfirmation' message.

    Unit sends confirmation that certificates ware installed.
    """

    message_type: Annotated[
        Literal['installUnitCertificatesConfirmation'],
        Field(
            alias='messageType',
            title='Message type',
            description='Message body type.',
        ),
    ]

    certificates: Annotated[
        list[AosInstallCertDataV7],
        Field(
            alias='certificates',
            title='Request to issue certificates',
            description='Request to issue certificates.',
        ),
    ]
