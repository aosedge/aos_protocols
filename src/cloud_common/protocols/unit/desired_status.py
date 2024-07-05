#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
import base64
from datetime import time
from typing import Annotated, Literal

from pydantic import Base64Bytes, BaseModel, Field, field_serializer

from cloud_common.protocols.unit.types import (
    AosSensitiveBytes,
    TypeAosFileSize,
    TypeAosSha256,
    TypeAosUrlsList,
    TypeComponentAnnotationsOptional,
    TypeComponentIdOptional,
    TypeComponentType,
    TypeLayerDigest,
    TypeLayerIdMandatory,
    TypeNodeDesiredStatus,
    TypeNodeIdMandatory,
    TypeProviderIdMandatory,
    TypeServiceIdMandatory,
    TypeServiceServiceIdMandatory,
    TypeSubjectSubjectIdMandatory,
    TypeVersionMandatory,
)
from cloud_common.protocols.unit.unit_config import UnitConfig


class AosReceiverInfo(BaseModel):
    """Information about receiver certificate."""

    serial: Annotated[
        str,
        Field(
            description='Certificate serial number.',
        ),
    ]

    issuer: Annotated[
        Base64Bytes,
        Field(
            description='Certificate `Issuer DN` field bytes.',
        ),
    ]


class AosDecryptionInfo(BaseModel):
    """Information for the decryption."""

    block_alg: Annotated[
        Literal['AES256/CBC/pkcs7'],
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

    asym_alg: Annotated[
        Literal['RSA/PKCS1v1_5', 'RSA/PSS'],
        Field(
            default='RSA/PKCS1v1_5',
            alias='asymAlg',
            description='Used asymmetric cipher in form: `cipher/padding`.',
        ),
    ]

    receiver_info: Annotated[
        AosReceiverInfo,
        Field(
            alias='receiverInfo',
            description='Receiver info to detect used key.',
        ),
    ]

    @field_serializer('block_key', 'block_iv', when_used='json')
    def dump_secret(self, struct_value):
        return base64.b64encode(struct_value.get_secret_value())


TypeAosDecryptionInfo = Annotated[
    AosDecryptionInfo,
    Field(
        alias='decryptionInfo',
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
        alias='signs',
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


class AosScheduleRule(BaseModel):
    """Aos schedule rule."""

    ttl: Annotated[
        int,
        Field(
            default=None,
            description='TTL of the rule in seconds.',
        ),
    ]

    type: Annotated[
        Literal['force', 'trigger', 'timetable'],
        Field(
            description='Type of the Schedule rule.',
        ),
    ]

    timetable: Annotated[
        list[AosTimetableItem],
        Field(
            default=None,
            description='Timetable when rule must work (only when the type is `timetable`).',
        ),
    ]


class AosDesiredComponentInfo(BaseModel):
    """Component info sent from the AosEdge Cloud."""

    id: TypeComponentIdOptional
    type: TypeComponentType
    version: TypeVersionMandatory
    annotations: TypeComponentAnnotationsOptional
    urls: TypeAosUrlsList
    sha256: TypeAosSha256
    size: TypeAosFileSize
    decryption_info: TypeAosDecryptionInfo
    signs: TypeAosSignInfo


class AosDesiredLayerInfo(BaseModel):
    """Layer info sent from the AosEdge Cloud."""

    id: TypeLayerIdMandatory
    version: TypeVersionMandatory
    digest: TypeLayerDigest
    urls: TypeAosUrlsList
    sha256: TypeAosSha256
    size: TypeAosFileSize
    decryption_info: TypeAosDecryptionInfo
    signs: TypeAosSignInfo


class AosDesiredServiceInfo(BaseModel):
    """Service info sent from the AosEdge Cloud."""

    service_id: TypeServiceIdMandatory
    provider_id: TypeProviderIdMandatory
    version: TypeVersionMandatory
    urls: TypeAosUrlsList
    sha256: TypeAosSha256
    size: TypeAosFileSize
    decryption_info: TypeAosDecryptionInfo
    signs: TypeAosSignInfo


class AosDesiredInstanceInfo(BaseModel):
    """Service info sent from the AosEdge Cloud."""

    service_id: TypeServiceServiceIdMandatory
    subject_id: TypeSubjectSubjectIdMandatory

    priority: Annotated[
        int,
        Field(
            default=0,
            ge=0,
            lt=1000000,  # noqa: WPS432
            description='Priority of the service instance.',
        ),
    ]

    num_instances: Annotated[
        int,
        Field(
            alias='numInstances',
            default=1,
            gt=0,
            description='Number of service instances to run.',
        ),
    ]

    labels: Annotated[
        list[str],
        Field(
            default=None,
            description='Label list associated with the service.',
        ),
    ]


class AosNodeDesiredState(BaseModel):
    """Desired node status."""

    node_id: TypeNodeIdMandatory
    state: TypeNodeDesiredStatus


class AosDesiredStatus(BaseModel):
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
        UnitConfig,
        Field(
            default=None,
            alias='unitConfig',
            description='Desired unit config dictionary.',
        ),
    ]

    components: Annotated[
        list[AosDesiredComponentInfo],
        Field(
            default=None,
            description='List of the desired components.',
        ),
    ]

    layers: Annotated[
        list[AosDesiredLayerInfo],
        Field(
            default=None,
            description='List of the desired layers.',
        ),
    ]

    services: Annotated[
        list[AosDesiredServiceInfo],
        Field(
            default=None,
            description='List of the desired services. If absent or null - do nothing.',
        ),
    ]

    instances: Annotated[
        list[AosDesiredInstanceInfo],
        Field(
            default=None,
            description='List of the desired services instances. If absent or null - do nothing.',
        ),
    ]

    fota_schedule: Annotated[
        AosScheduleRule,
        Field(
            alias='fotaSchedule',
            default=None,
            description='Points to rules when FOTA can be applied.',
        ),
    ]

    sota_schedule: Annotated[
        AosScheduleRule,
        Field(
            alias='sotaSchedule',
            default=None,
            description='Points to rules when SOTA can be applied.',
        ),
    ]

    certificates: Annotated[
        list[AosCertificateInfo],
        Field(
            default=None,
            description='The list of the used certificates',
        ),
    ]

    certificate_chains: Annotated[
        list[AosCertificateChainInfo],
        Field(
            default=None,
            alias='certificateChains',
            description='Certificate chains info for checking signs.',
        ),
    ]
