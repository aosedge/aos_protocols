#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
import base64
from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, Field, field_serializer

from cloud_common.protocols.unit.types import (
    AosSensitiveBytes,
    TypeCertificatesType,
    TypeNodeIdMandatory,
    TypeStatusForNonExecutables,
)


class AosCertificateIdentification(BaseModel):
    """Certificate identification data."""

    type: TypeCertificatesType
    node_id: TypeNodeIdMandatory


class AosCertificateIdentificationValidTill(AosCertificateIdentification):
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


class AosUnitSecretData(BaseModel):
    """Keeps unit secret used to decode secure device password."""

    owner_password: Annotated[
        AosSensitiveBytes,
        Field(
            default=None,
            alias='ownerPassword',
            title='Owner Password',
            description='The owner password.',
        ),
    ]

    @field_serializer('owner_password', when_used='json')
    def dump_secret(self, struct_value):
        if not struct_value:
            return None
        return base64.b64encode(struct_value.get_secret_value())


class AosUnitSecret(BaseModel):
    """Keeps the unit secret used to decode secure device information."""

    version: Annotated[
        int,
        Field(
            alias='version',
            title='Version',
            description='Version of the unit secrets.',
        ),
    ]

    data: Annotated[  # noqa: WPS110
        AosUnitSecretData,
        Field(
            default=None,
            alias='data',
            title='Data of the unit secret.',
            description='Data of the unit secret.',
        ),
    ]


class AosRenewCertsNotification(BaseModel):
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
        list[AosCertificateIdentificationValidTill],
        Field(
            alias='certificates',
            title='Certificates',
            description='The list of certificates that were renewed.',
        ),
    ]

    unit_secret: Annotated[
        AosUnitSecret,
        Field(
            alias='unitSecret',
            title='Unit Secret',
            description='The unit Secret',
        ),
    ]


class AosIssuedUnitCerts(AosCertificateIdentification):
    """IssuedUnitCerts issued unit certificates info."""

    certificate_chain: Annotated[
        str,
        Field(
            alias='certificateChain',
            title='Chain of certificates',
            description='Chain of certificates.',
        ),
    ]


class AosIssuedUnitCertificates(BaseModel):
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
        list[AosIssuedUnitCerts],
        Field(
            alias='certificates',
            title='Certificates',
            description='The list of certificates that were issued.',
        ),
    ]


class AosIssueCertData(AosCertificateIdentification):
    """IssueCertData issue certificate data."""

    csr: Annotated[
        str,
        Field(
            alias='csr',
            title='CSR',
            description='Certificate Signing Request.',
        ),
    ]


class AosIssueUnitCertificates(BaseModel):
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


class AosInstallCertData(AosCertificateIdentification):
    """InstallCertData install certificate data."""

    serial: Annotated[
        str,
        Field(
            alias='serial',
            title='Serial of the Certificate',
            description='Serial of the Certificate.',
        ),
    ]
    status: TypeStatusForNonExecutables
    description: Annotated[
        str,
        Field(
            default=None,
            alias='description',
            title='Description',
            description='Description of the Certificate Installation',
        ),
    ]


class AosInstallUnitCertificatesConfirmation(BaseModel):
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
        list[AosInstallCertData],
        Field(
            alias='certificates',
            title='Request to issue certificates',
            description='Request to issue certificates.',
        ),
    ]
