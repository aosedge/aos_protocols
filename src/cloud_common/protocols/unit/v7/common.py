#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Optional, Literal, List
from uuid import UUID

from pydantic import Field

from .types import AosBaseModel
from ..common import (
    AosErrorInfo,
    AosHostRecord,
    AosIdentityType,
)


class AosBaseDataModel(AosBaseModel):
    """Base model for Aos objects."""

    correlation_id: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='correlationId',
            description='Correlation ID of the request.',
        ),
    ] = None


class AosIdentity(AosBaseModel):
    """Aos objects identifier."""

    id: Annotated[
        Optional[UUID],
        Field(
            default=None,
            alias='id',
            title='Aos object UUID identifier. Unique per Aos instance.',
            description='Aos object unique per Aos instance UUID.',
        ),
    ] = None

    type: Annotated[
        Optional[AosIdentityType],
        Field(
            default=None,
            alias='type',
            title='Aos object type.',
            description='Aos object type. E.g.: AosService, AosComponent',
        ),
    ] = None

    codename: Annotated[
        Optional[str],
        Field(
            default=None,
            title='Aos object codename.',
            description='Aos object codename. Uniqueness depends on object type.',
        ),
    ] = None

    title: Annotated[
        Optional[str],
        Field(
            default=None,
            title='Aos object title.',
            description='Aos object title.',
        ),
    ] = None

    description: Annotated[
        Optional[str],
        Field(
            default=None,
            title='Aos object description.',
            description='Aos object description.',
        ),
    ] = None

    urn: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='urn',
            title='Aos object URN.',
            description='Aos object URN. Globally unique.',
        ),
    ] = None


class AosResourceInfo(AosBaseModel):

    name: Annotated[
        str,
        Field(
            alias='name',
            description='The name of the resource.',
            examples=['camera0', 'shared_folder_1', 'dbus'],
        ),
    ]

    shared_count: Annotated[
        int,
        Field(
            alias='sharedCount',
            ge=0,
            description='The number of maximum shared usages. 0 mean unlimited',
        ),
    ]


class AosOsInfo(AosBaseModel):

    os: Annotated[
        str,
        Field(
            alias='os',
            examples=['linux'],
        ),
    ]

    version: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='version',
            description='The version of the OS.',
            examples=['6.8.0'],
        ),
    ] = None

    features: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            alias='features',
            description='This OPTIONAL property specifies an array of strings, each specifying a mandatory OS feature.',
        ),
    ] = None


class AosArchInfo(AosBaseModel):

    architecture: Annotated[
        str,
        Field(
            alias='architecture',
            description='The architecture of the CPU. '
                        'Refer to the "https://github.com/opencontainers/image-spec/blob/main/config.md#properties"',
            examples=['amd64', 'arm64', 'arm'],
        ),
    ]

    variant: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='variant',
            description='The variant of the specified CPU architecture. '
                        'Refer to the "https://github.com/opencontainers/image-spec/blob/main/config.md#properties"',
        ),
    ]


class AosUpdateItemImageInfo(AosBaseModel):

    digest: Annotated[
        UUID,
        Field(
            alias='id',
            description='The identification of the update item image.',
        ),
    ]

    arch_info: Annotated[
        AosArchInfo,
        Field(
            alias='archInfo',
            description='The architecture of the update item image.',
        ),
    ]

    os_info: Annotated[
        AosOsInfo,
        Field(
            alias='osInfo',
            description='The OS of the update item image.',
        ),
    ]


class AosSubject(AosBaseModel):

    identity: Annotated[
        AosIdentity,
        Field(
            alias='identity',
            description='The identification of the subject.',
        ),
    ]

    type: Annotated[
        Literal['group', 'user'],
        Field(
            alias='type',
            description='The type of the subject.',
        ),
    ]


TypeAosIdentityMandatory = Annotated[
    AosIdentity,
    Field(
        alias='identity',
        description='The identification of the resource.',
    ),
]


TypeItemMandatory = Annotated[
    AosIdentity,
    Field(
        alias='item',
        description='Update item identifier.',
    ),
]


TypeAosIdentityOptional = Annotated[
    Optional[AosIdentity],
    Field(
        default=None,
        alias='identity',
        description='The identification of the resource.',
    ),
]


TypeItemOptional = Annotated[
    Optional[AosIdentity],
    Field(
        default=None,
        alias='item',
        description='Update item identifier.',
    ),
]


TypeSubjectMandatory = Annotated[
    AosIdentity,
    Field(
        alias='subject',
        title='Subject ID',
        description='Unique ID of the subject.',
    ),
]


__all__ = (
    'AosBaseDataModel',
    'AosArchInfo',
    'AosOsInfo',
    'AosIdentity',
    'AosErrorInfo',
    'AosHostRecord',
    'AosResourceInfo',
    'AosUpdateItemImageInfo',
    'TypeAosIdentityMandatory',
    'TypeAosIdentityOptional',
    'TypeItemMandatory',
    'TypeItemOptional',
    'AosSubject',
    'TypeSubjectMandatory',
)
