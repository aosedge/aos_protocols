#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Literal, Optional

from pydantic import Base64Bytes, Field, Secret, UUID4, BaseModel, ConfigDict

from cloud_common.protocols.unit.constants import DataSizes


class AosBaseModel(BaseModel):

    model_config = ConfigDict(
        validate_by_name=True,
        serialize_by_alias=True,
        use_enum_values=True,
        populate_by_name=True,
    )


TypeIdentifierIdOptional = Annotated[
    UUID4,
    Field(
        None,
        alias='id',
        title='Identifier ID',
        description='ID of the object, type: UUID.',
    ),
]


TypeStatusForNonExecutables = Annotated[
    Literal[
        'installed',
        'downloading',
        'failed',
        'error',
    ],
    Field(
        description='current status of the item',
    ),
]

TypeAosSystemUidMandatory = Annotated[
    str,
    Field(
        alias='system_uid',
        description='UID of the Unit',
    ),
]

TypeAosSystemIdMandatory = Annotated[
    str,
    Field(
        alias='systemId',
        title='',
        description='The unique system ID of the unit.',
    ),
]

TypeVersionMandatory = Annotated[
    str,
    Field(
        alias='version',
        description='Version in format of the SemVer.',
    ),
]

TypeVersionOptional = Annotated[
    str,
    Field(
        default=None,
        alias='version',
        description='Version in format of the SemVer.',
    ),
]

TypeNodeIdMandatory = Annotated[
    str,
    Field(
        alias='nodeId',
        title='Node ID',
        description='Unique ID of the node.',
    ),
]

TypeNodeIdOptional = Annotated[
    str,
    Field(
        default=None,
        alias='nodeId',
        title='Node ID',
        description='Unique ID of the node',
    ),
]

TypeNodeTypeMandatory = Annotated[
    str,
    Field(
        alias='nodeType',
        title='Node Type',
        description='Group of nodes with identical configuration.',
    ),
]

TypeLayerIdMandatory = Annotated[
    str,
    Field(
        alias='id',
        description='Unique ID of the layer',
        examples=['python3.12-libs'],
    ),
]

TypeSubjectIdMandatory = Annotated[
    str,
    Field(
        alias='id',
        description='Unique ID of the subject',
    ),
]

TypeSubjectSubjectIdMandatory = Annotated[
    str,
    Field(
        alias='subjectId',
        title='Subject ID',
        description='Unique ID of the subject.',
    ),
]

TypeSubjectSubjectIdOptional = Annotated[
    str,
    Field(
        default=None,
        alias='subjectId',
        title='Subject ID',
        description='Unique ID of the subject.',
    ),
]

TypeInstanceNoMandatory = Annotated[
    int,
    Field(
        alias='instance',
        title='Instance no',
        description='The instance number of the service. Starts from 0.',
    ),
]

TypeInstanceNoOptional = Annotated[
    int,
    Field(
        default=None,
        alias='instance',
        title='Instance no',
        description='The instance number of the service. Starts from 0.',
    ),
]

TypeProviderIdMandatory = Annotated[
    str,
    Field(
        alias='providerId',
        description='Unique ID of the service provider',
    ),
]

TypeDeviceMandatory = Annotated[
    str,
    Field(
        alias='deviceId',
        description='Device name on a Unit',
    ),
]

TypeAlertMessageMandatory = Annotated[
    str,
    Field(
        min_length=1,
        max_length=DataSizes.MAX_ALERT_MESSAGE_LENGTH,
        description='Error information retrieved for the alert.',
    ),
]

TypeCoreComponentIdMandatory = Annotated[
    str,
    Field(
        alias='coreComponent',
        min_length=1,
        max_length=DataSizes.MAX_COMPONENT_ID_LENGTH,
        description='Error information retrieved for the alert.',
    ),
]

TypeComponentId = Annotated[
    str,
    Field(
        alias='id',
        title='Component ID',
        description='Component unique identifier.',
    ),
]

TypeComponentIdOptional = Annotated[
    Optional[str],
    Field(
        alias='id',
        default=None,
        title='Component ID',
        description='Component unique identifier.',
    ),
]

TypeComponentType = Annotated[
    str,
    Field(
        alias='type',
        title='Component type ID',
        description='Component unique type identifier',
        examples=['rootfs', 'bios'],
    ),
]

TypeComponentAnnotationsOptional = Annotated[
    dict,
    Field(
        default=None,
        alias='annotations',
        description='Additional information about this component',
    ),
]

TypeAosUrlsList = Annotated[
    list[str],
    Field(
        alias='urls',
        description='the list of urls pointer to the same target',
        min_length=1,
    ),
]

TypeAosSha256 = Annotated[
    Base64Bytes,
    Field(
        alias='sha256',
        description='SHA256 digest of the target',
    ),
]

TypeStateChecksumOptional = Annotated[
    Optional[Base64Bytes],
    Field(
        default=None,
        alias='stateChecksum',
        description='The checksum of the state. This Base64 of sha256 digest over the state.',
    ),
]

TypeAosFileSize = Annotated[
    int,
    Field(
        alias='size',
        description='size of the file in bytes',
    ),
]

TypeAosLogId = Annotated[
    str,
    Field(
        alias='logId',
        title='Lod Request ID',
        description='The unique log request ID. Used to group all results into the single batch.',
    ),
]

AosSensitiveBytes = Secret[Base64Bytes]

TypeCertificatesType = Annotated[
    Literal['offline', 'online', 'um', 'sm', 'cm', 'iam', 'host-device', 'remote-device', 'azure-iot'],
    Field(
        alias='type',
        title='Type of the certificate',
        description='Type of the certificate.',
    ),
]

TypeNodeState = Annotated[
    Literal[
        'unprovisioned',
        'provisioned',
        'error',
        'paused',
    ],
    Field(
        alias='state',
        description='The current (reported) status of the node.',
    ),
]

TypeNodeDesiredStatus = Annotated[
    Literal[
        'provisioned',
        'paused',
    ],
    Field(
        alias='status',
        description='The desired status of the node.',
    ),
]


TypeUpdateItemState = Annotated[
    Literal[
        'unknown',
        'downloading',
        'pending',
        'installing',
        'installed',
        'removing',
        'removed',
        'failed',
    ],
    Field(
        alias='state',
        description='The current (reported) state of the update item.',
    ),
]


TypeUpdateItemInstanceState = Annotated[
    Literal[
        'activating',
        'active',
        'inactive',
        'failed',
    ],
    Field(
        alias='state',
        description='The current (reported) state of the service instance.',
    ),
]


TypeLayerDigest = Annotated[
    str,
    Field(
        alias='digest',
        description='Digest of the layer.',
    ),
]


TypeUrnMandatory = Annotated[
    str,
    Field(
        alias='urn',
        title='URN of the object',
        description='Unique URN of the object.',
    ),
]


TypeNodeDesiredState = Annotated[
    Literal[
        'provisioned',
        'paused',
    ],
    Field(
        alias='state',
        description='The desired state of the node.',
    ),
]
