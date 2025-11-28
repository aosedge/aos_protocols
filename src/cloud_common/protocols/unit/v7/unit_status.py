#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Dict, Literal, Optional, List

from pydantic import BaseModel, Field, UUID4

from .common import AosIdentity, AosResourceInfo, AosArchInfo, AosOsInfo, TypeItemMandatory, TypeSubjectMandatory, \
    AosBaseModel
from ..common import TypeAosErrorInfoOptional
from .types import (
    TypeInstanceNoMandatory,
    TypeNodeState,
    TypeUpdateItemInstanceState,
    TypeStateChecksumOptional,
    TypeVersionMandatory,
    TypeVersionOptional,
    TypeUpdateItemState,
)


class AosUnitConfigStatus(BaseModel):
    version: TypeVersionOptional
    state: Annotated[
        Literal[
            'absent',
            'installed',
            'failed',
        ],
        Field(
            description='current state of the item',
        ),
    ]
    error_info: TypeAosErrorInfoOptional


class AosNodePartitionInfo(BaseModel):
    """Aos node partition info."""

    name: Annotated[
        str,
        Field(
            title='Name',
            alias='name',
        ),
    ]

    types: Annotated[
        list[str],
        Field(
            title='List of types',
            alias='types',
        ),
    ]

    total_size: Annotated[
        int,
        Field(
            title='Total size',
            alias='totalSize',
        ),
    ]


class AosNodeCPUInfo(BaseModel):

    cpu_model_name: Annotated[
        str,
        Field(
            default=None,
            alias='modelName',
        ),
    ]

    total_num_cores: Annotated[
        int,
        Field(
            default=None,
            alias='totalNumCores',
        ),
    ]

    total_num_threads: Annotated[
        int,
        Field(
            default=None,
            alias='totalNumThreads',
        ),
    ]

    arch_info: Annotated[
        AosArchInfo,
        Field(
            alias='archInfo',
        ),
    ]

    max_dmips: Annotated[
        Optional[int],
        Field(
            alias='maxDmips',
        ),
    ] = None


class AosRuntimeInfo(BaseModel):

    identity: Annotated[
        AosIdentity,
        Field(
            alias='identity',
        ),
    ]

    runtime_type: Annotated[
        str,
        Field(
            alias='runtimeType',
            min_length=1,
            max_length=64,
            examples=[
                'runc',
                'crun',
                'break_system_controllers_bs351',
                'bios',
                '',
            ]
        ),
    ]

    arch_info: Annotated[
        AosArchInfo,
        Field(
            alias='archInfo',
        ),
    ]

    os_info: Annotated[
        AosOsInfo,
        Field(
            alias='osInfo',
        ),
    ]

    max_dmips: Annotated[
        Optional[int],
        Field(
            default=None,
            alias='maxDmips',
        ),
    ]

    allowed_dmips: Annotated[
        Optional[int],
        Field(
            default=None,
            alias='allowedDmips',
        ),
    ]

    total_ram: Annotated[
        Optional[int],
        Field(
            default=None,
            alias='totalRam',
            description='Total memory in bytes. None if runner shares memory with node.',
        ),
    ]

    allowed_ram: Annotated[
        Optional[int],
        Field(
            default=None,
            alias='allowedRam',
            description='Memory that can be used to run services in bytes. None if no restrictions.',
        ),
    ]

    max_instances: Annotated[
        int,
        Field(
            alias='maxInstances',
            ge=0,
            description='The maximum number of instances. 0 for unlimited.',
        ),
    ]


class AosUnitNodeInfo(BaseModel):

    identity: Annotated[
        AosIdentity,
        Field(
            description='Identifier of the node.',
            examples=[{"codename": "node-1398431", "title": "DomD"}],
        )
    ]

    node_group_subject: Annotated[
        AosIdentity,
        Field(
            alias='nodeGroupSubject',
            description='Subject of the node group. Previously known as NodeType.',
            examples=[{"codename": "main-node"}],
        ),
    ]

    max_dmips: Annotated[
        int,
        Field(
            alias='maxDmips',
        ),
    ]

    physical_ram: Annotated[
        Optional[int],
        Field(
            default=None,
            alias='physicalRam',
            description='Total physical node RAM in bytes.',
            ge=1,
        ),
    ]

    total_ram: Annotated[
        int,
        Field(
            alias='totalRam',
            description='Total node RAM in bytes (physical + swap).',
            ge=1,
        ),
    ]

    os_info: Annotated[
        AosOsInfo,
        Field(
            alias='osInfo',
        ),
    ]

    cpus: Annotated[
        Optional[list[AosNodeCPUInfo]],
        Field(
            default=None,
            alias='cpus',
        ),
    ] = None

    attrs: Annotated[
        Optional[Dict[str, str]],
        Field(
            default=None,
            alias='attrs',
            examples=[{'dynamic'}, {'static': '', 'cloud_connection': '', 'name1': 'value1'}],
        ),
    ] = None

    partitions: Annotated[
        list[AosNodePartitionInfo],
        Field(
            alias='partitions',
            default=None,
            description='List of partitions',
        ),
    ]

    runtimes: Annotated[
        Optional[List[AosRuntimeInfo]],
        Field(
            default=None,
            alias='runtimes',
            description='List of supported runtimes.',
        ),
    ]

    resources: Annotated[
        Optional[List[AosResourceInfo]],
        Field(
            default=None,
            description='List of available resources.',
        ),
    ]

    provisioned: Annotated[
        bool,
        Field(
            alias='provisioned',
            description='Flag to indicate if the node is provisioned.',
        ),
    ]

    state: TypeNodeState
    error_info: TypeAosErrorInfoOptional


class AosInstanceInfo(BaseModel):

    node: Annotated[
        AosIdentity,
        Field(
            alias='node',
        ),
    ]

    runtime: Annotated[
        AosIdentity,
        Field(
            alias='runtime',
        ),
    ]

    instance: TypeInstanceNoMandatory
    state_checksum: TypeStateChecksumOptional
    state: TypeUpdateItemInstanceState
    error_info: TypeAosErrorInfoOptional


class AosInstancesInfo(BaseModel):
    """Update item info sent to the AosEdge Cloud."""

    item: TypeItemMandatory
    subject: TypeSubjectMandatory
    version: TypeVersionMandatory

    instances: Annotated[
        List[AosInstanceInfo],
        Field(
            alias='instances',
        ),
    ]


class AosUpdateItemInfo(BaseModel):
    """Update item info sent to the AosEdge Cloud."""

    item: TypeItemMandatory
    version: TypeVersionMandatory

    state: TypeUpdateItemState
    error_info: TypeAosErrorInfoOptional


class AosUnitStatusV7(AosBaseModel):
    """
    AosUnit protocol: 'unitStatus' message.

    Unit reports all current status information using this message
    """

    message_type: Annotated[
        Literal['unitStatus'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    is_delta_info: Annotated[
        Optional[bool],
        Field(
            default=None,
            alias='isDeltaInfo',
            title='Delta info?',
            description='Flag to indicate if this is a full info message or delta from previous times',
            examples=[True, False],
        ),
    ]

    unit_config: Annotated[
        Optional[list[AosUnitConfigStatus]],
        Field(
            default=None,
            alias='unitConfig',
            description='Information about the installed unitConfig.',
        ),
    ]

    nodes: Annotated[
        Optional[list[AosUnitNodeInfo]],
        Field(
            default=None,
            alias='nodes',
            description='The list of attached to the Unit nodes.',
        ),
    ]

    items: Annotated[
        Optional[list[AosUpdateItemInfo]],
        Field(
            default=None,
            alias='items',
            description='List of the Aos update items.',
        ),
    ]

    instances: Annotated[
        Optional[list[AosInstancesInfo]],
        Field(
            default=None,
            alias='instances',
        ),
    ]

    subjects: Annotated[
        Optional[list[AosIdentity]],
        Field(
            default=None,
            alias='subjects',
        ),
    ]
