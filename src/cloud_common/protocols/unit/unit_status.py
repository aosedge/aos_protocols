#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from typing import Annotated, Dict, Literal, Optional

from pydantic import BaseModel, Field

from .common import TypeAosErrorInfoOptional
from .constants import DataSizes
from .types import (
    TypeComponentAnnotationsOptional,
    TypeComponentId,
    TypeInstanceNoMandatory,
    TypeLayerDigest,
    TypeLayerIdMandatory,
    TypeLayerStatus,
    TypeNodeIdMandatory,
    TypeNodeStatus,
    TypeServiceIdMandatory,
    TypeServiceInstanceStatus,
    TypeServiceServiceIdMandatory,
    TypeServiceStatus,
    TypeStateChecksumOptional,
    TypeStatusForNonExecutables,
    TypeSubjectSubjectIdMandatory,
    TypeVersionMandatory,
    TypeVersionOptional,
)


class AosUnitConfigStatus(BaseModel):
    version: TypeVersionOptional
    status: TypeStatusForNonExecutables
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
    arch: Annotated[
        str,
        Field(
            alias='arch',
            examples=['x86', 'x86_64', 'arm32', 'arm64'],
        ),
    ]
    arch_family: Annotated[
        Optional[str],
        Field(
            alias='archFamily',
            examples=['ARMv7', 'ARMv8', 'ARMv9'],
        ),
    ] = None

    max_dmips: Annotated[
        Optional[int],
        Field(
            alias='maxDmips',
        ),
    ] = None


class AosUnitNodeInfo(BaseModel):
    id: Annotated[
        str,
        Field(
            alias='id',
            min_length=1,
            max_length=DataSizes.DATA_LENGTH_256,
            description='Node unique identifier',
            examples=['1398jf391', 'node0'],
        ),
    ]

    name: Annotated[
        Optional[str],
        Field(
            alias='name',
            max_length=DataSizes.DATA_LENGTH_256,
            description='User-friendly name of the node',
            examples=['Dom0', 'DomD'],
        ),
    ]

    type: Annotated[
        str,
        Field(
            alias='type',
            min_length=1,
            max_length=DataSizes.DATA_LENGTH_256,
        ),
    ]

    max_dmips: Annotated[
        int,
        Field(
            alias='maxDmips',
        ),
    ]

    cpus: Annotated[
        Optional[list[AosNodeCPUInfo]],
        Field(
            alias='cpus',
        ),
    ]

    os_type: Annotated[
        str,
        Field(
            alias='osType',
        ),
    ]

    attrs: Annotated[
        Optional[Dict[str, str]],
        Field(
            default=None,
            alias='attrs',
            examples=[{'dynamic'}, {'static': '', 'cloud_connection': '', 'name1': 'value1'}],
        ),
    ]

    total_ram: Annotated[
        int,
        Field(
            alias='totalRam',
            ge=1,
        ),
    ]

    partitions: Annotated[
        list[AosNodePartitionInfo],
        Field(
            alias='partitions',
            default=None,
            description='List of partitions',
        ),
    ]

    status: TypeNodeStatus
    error_info: TypeAosErrorInfoOptional


class AosComponentInfo(BaseModel):
    """
    Aos component info.

    AosEdge uses this struct to report information about Unit's components
    """

    id: TypeComponentId

    type: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='type',
            description='type of the component',
        ),
    ]

    version: TypeVersionMandatory

    node_id: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='nodeId',
            description='IDs list of nodes this component is part of. Can be omitted for some statuses',
        ),
    ]

    status: TypeStatusForNonExecutables
    annotations: TypeComponentAnnotationsOptional
    error_info: TypeAosErrorInfoOptional


class AosLayerStatusInfo(BaseModel):
    """Layer status info."""

    layer_id: TypeLayerIdMandatory
    version: TypeVersionMandatory
    digest: TypeLayerDigest
    status: TypeLayerStatus
    error_info: TypeAosErrorInfoOptional


class AosServiceStatus(BaseModel):
    """Reported by a unit service status."""

    service_id: TypeServiceIdMandatory
    version: TypeVersionMandatory
    status: TypeServiceStatus
    error_info: TypeAosErrorInfoOptional


class AosServiceInstanceStatus(BaseModel):
    """Reported by a unit service instance status."""

    service_id: TypeServiceServiceIdMandatory
    subject_id: TypeSubjectSubjectIdMandatory
    instance: TypeInstanceNoMandatory
    version: TypeVersionMandatory
    node_id: TypeNodeIdMandatory
    status: TypeServiceInstanceStatus
    state_checksum: TypeStateChecksumOptional
    error_info: TypeAosErrorInfoOptional


class AosUnitStatus(BaseModel):
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
        list[AosUnitConfigStatus],
        Field(
            default=None,
            alias='unitConfig',
            description='Information about the installed unitConfig.',
        ),
    ]

    nodes: Annotated[
        list[AosUnitNodeInfo],
        Field(
            default=None,
            alias='nodes',
            description='The list of attached to the Unit nodes.',
        ),
    ]

    services: Annotated[
        list[AosServiceStatus],
        Field(
            default=None,
            alias='services',
            desctiption='Information about the services present in this unit.',
        ),
    ]

    instances: Annotated[
        list[AosServiceInstanceStatus],
        Field(
            default=None,
            alias='instances',
        ),
    ]

    layers: Annotated[
        list[AosLayerStatusInfo],
        Field(
            default=None,
            alias='layers',
        ),
    ]

    components: Annotated[
        list[AosComponentInfo],
        Field(
            default=None,
            alias='components',
            description='information about all components located on the unit.',
        ),
    ]

    unit_subjects: Annotated[
        list[str],
        Field(
            default=None,
            alias='unitSubjects',
        ),
    ]
