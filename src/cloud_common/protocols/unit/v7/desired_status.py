#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
import base64
from datetime import time
from typing import Annotated, Literal, Optional, List

from pydantic import Base64Bytes, BaseModel, Field, field_serializer

from cloud_common.protocols.unit.types import (
    AosSensitiveBytes,
    TypeAosFileSize,
    TypeAosSha256,
    TypeAosUrlsList,
    TypeVersionMandatory,
)

from .common import AosIdentity, TypeItemMandatory, AosSubject, AosBaseModel
from .types import TypeNodeDesiredState
from .unit_config import UnitConfigV7


class AosDecryptInfo(BaseModel):
    """Information for the decryption."""

    block_alg: Annotated[
        Literal[
            'AES256/CBC/pkcs7',
            'AES256/GCM/',
        ],
        Field(
            default='AES256/CBC/pkcs7',
            alias='blockAlg',
            description='Used block cipher in form: `cipher/mode/padding`.',
        ),
    ]

    block_iv: Annotated[
        AosSensitiveBytes,
        Field(
            alias='blockIv',
            description='Initialization vector for encryption/decryption.',
        ),
    ]

    block_key: Annotated[
        AosSensitiveBytes,
        Field(
            alias='blockKey',
            description='Symmetric block key value.',
        ),
    ]

    @field_serializer('block_key', 'block_iv', when_used='json')
    def dump_secret(self, struct_value):
        return base64.b64encode(struct_value.get_secret_value())


TypeAosDecryptInfo = Annotated[
    AosDecryptInfo,
    Field(
        alias='decryptInfo',
        description='Object with information to decrypt the component.',
    ),
]


class AosCertificateInfo(BaseModel):
    """Certificate content and fingerprint."""

    certificate: Annotated[
        Base64Bytes,
        Field(
            description='Base64 encoded certificate in the `der` form.',
        ),
    ]

    fingerprint: Annotated[
        str,
        Field(
            description='Fingerprint of the certificate (unique ID)',
        ),
    ]


class AosCertificateChainInfo(BaseModel):
    """Certificate content and fingerprint."""

    name: Annotated[
        str,
        Field(
            description='Unique name of the certificate chain.',
        ),
    ]

    fingerprints: Annotated[
        list[str],
        Field(
            description='Fingerprint list of the certificates included in the chain.',
        ),
    ]


class AosSignInfo(BaseModel):
    """Aos sign information."""

    chain_name: Annotated[
        str,
        Field(
            alias='chainName',
            description='chain name from the list of `certificateChains`.',
        ),
    ]

    alg: Annotated[
        Literal['RSA/SHA256', 'EC/SHA256'],
        Field(
            description='Used algorithm for signing in the form `alg/hash`.',
        ),
    ]

    value: Annotated[  # noqa: WPS110
        str,
        Field(
            description='Base64 encoded value of the signature.',
        ),
    ]

    trusted_timestamp: Annotated[
        str,
        Field(
            alias='trustedTimestamp',
            description='Timestamp of the signature in ISO8601 format.',
        ),
    ]

    ocsp_values: Annotated[
        list[str],
        Field(
            alias='ocspValues',
            default=None,
            description='OCSP value of the signature.',
        ),
    ]


TypeAosSignInfo = Annotated[
    AosSignInfo,
    Field(
        alias='signInfo',
        description='Sign values of the file.',
    ),
]


class AosTimeSlot(BaseModel):
    """Timetable time slot."""

    start: Annotated[
        time,
        Field(
            description='Start time in form `HH:MM[:SS]`.',
        ),
    ]

    end: Annotated[
        time,
        Field(
            description='End time in form `HH:MM[:SS]`.',
        ),
    ]


class AosTimetableItem(BaseModel):
    """
    Timetable signe record.

    Represent one entry of the timetable in form
    `day of week`: [start time:end time]
    """

    day_of_week: Annotated[
        int,
        Field(
            alias='dayOfWeek',
            description='Day of the week: Monday [1] ... Sunday [7].',
        ),
    ]

    time_slots: Annotated[
        list[AosTimeSlot],
        Field(
            alias='timeSlots',
            min_items=1,
            description='List of the time slots for the timetable.',
        ),
    ]


class AosUpdateItemBlobInfo(BaseModel):

    digest: Annotated[
        str,
        Field(
            alias='digest',
            description='The identification of the update item BLOB. Format same as OCI spec format',
            examples=['sha256:3c3a4604a545cdc127456d94e421cd355bca5b528f4a9c1905b15da2eb4a4c6b']
        ),
    ]

    urls: TypeAosUrlsList
    sha256: TypeAosSha256
    size: TypeAosFileSize
    decrypt_info: TypeAosDecryptInfo
    sign_info: TypeAosSignInfo


class AosUpdateItemInfo(BaseModel):
    """Update item info sent from the AosEdge Cloud."""

    identity: TypeItemMandatory
    version: TypeVersionMandatory

    owner: Annotated[
        AosIdentity,
        Field(
            alias='owner',
            description='The ID of the owner of the update item (OEM or SP identity).',
        ),
    ]

    index_digest: Annotated[
        str,
        Field(
            alias='indexDigest',
            min_length=1,
            description='Digest of the index.json file for the update item.',
        ),
    ]


class AosDesiredInstanceInfo(BaseModel):
    """Update item info sent from the AosEdge Cloud."""

    item: TypeItemMandatory
    subject: AosIdentity

    priority: Annotated[
        int,
        Field(
            default=0,
            ge=0,
            lt=1000000,  # noqa: WPS432
            description='Priority of the service instance.',
        ),
    ] = 0

    num_instances: Annotated[
        int,
        Field(
            alias='numInstances',
            default=1,
            gt=0,
            description='Number of service instances to run.',
        ),
    ] = 1

    labels: Annotated[
        Optional[list[str]],
        Field(
            default=None,
            description='Label list associated with the service.',
        ),
    ] = None


class AosNodeDesiredState(BaseModel):
    """Desired node status."""

    item: TypeItemMandatory
    state: TypeNodeDesiredState


class AosDesiredStatusV7(AosBaseModel):
    """
    AosUnit protocol: 'desiredStatus' message.

    Unit reports all current status information using this message
    """

    message_type: Annotated[
        Literal['desiredStatus'],
        Field(
            alias='messageType',
            description='Type of the message body.',
        ),
    ]

    nodes: Annotated[
        list[AosNodeDesiredState],
        Field(
            default=None,
            alias='nodes',
            description="The list of desired node's status.",
        ),
    ]

    unit_config: Annotated[
        UnitConfigV7,
        Field(
            default=None,
            alias='unitConfig',
            description='Desired unit config dictionary.',
        ),
    ]

    items: Annotated[
        list[AosUpdateItemInfo],
        Field(
            default=[],
            alias='items',
            description='List of the desired update items. If absent or null - do nothing.',
            min_length=0,
        ),
    ]

    instances: Annotated[
        list[AosDesiredInstanceInfo],
        Field(
            default=None,
            description='List of the desired update item instances. If absent or null - do nothing.',
        ),
    ]

    subjects: Annotated[
        list[AosSubject],
        Field(
            default=None,
            description='The list of the used subjects',
        )
    ]

    certificates: Annotated[
        list[AosCertificateInfo],
        Field(
            default=None,
            description='The list of the used certificates',
            max_length=32,
        ),
    ]

    certificate_chains: Annotated[
        list[AosCertificateChainInfo],
        Field(
            default=None,
            alias='certificateChains',
            description='Certificate chains info for checking signs.',
            max_length=8,
        ),
    ]


class AosRequestBlobUrlsV7(AosBaseModel):
    message_type: Annotated[
        Literal['requestBlobUrls'],
        Field(
            alias='messageType',
            description='Type of the message body.',
        ),
    ]

    digests: Annotated[
        list[str],
        Field(
            alias='digests',
            description='The identification of the update item BLOB. Format same as OCI spec format',
            examples=[['sha256:3c3a4604a545cdc127456d94e421cd355bca5b528f4a9c1905b15da2eb4a4c6b']]
        ),
    ]


class AosBlobUrlsV7(AosBaseModel):
    message_type: Annotated[
        Literal['blobUrls'],
        Field(
            alias='messageType',
            description='Type of the message body.',
        ),
    ]

    items: Annotated[
        list[AosUpdateItemBlobInfo],
        Field(
            alias='items',
            description='The identification of the update item BLOB. Format same as OCI spec format',
        ),
    ]
