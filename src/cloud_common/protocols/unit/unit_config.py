#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from typing import Annotated, Optional

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.common import (
    AosDeviceInfo,
    AosFileSystemMount,
    AosHostRecord,
)
from cloud_common.protocols.unit.types import (
    TypeNodeIdOptional,
    TypeNodeTypeMandatory,
    TypeVersionMandatory,
)


class AlertRulePercents(BaseModel):
    """
    Information about the threshold.

    Threshold is treated as a node resource limit for rebalancing.

    The `high` threshold for resource limits must be defined as the upper limit of resource usage.
      If a node's resource usage exceeds the highThreshold for a continuous period specified
      by the threshold `timeout`, the system initiates a rebalancing process to redistribute service instances,
      thereby preventing resource overutilization and maintaining system performance.

    Once rebalancing is triggered due to exceeding the `high` threshold,
      the system will only consider the rebalancing action complete and cease further rebalancing activities
      if the resource usage then decreases and stabilizes below the `low` threshold for a continuous period
      specified by the threshold `timeout`

    The low/high thresholds for resource limits are set in percentages.
    """

    min_threshold: Annotated[
        float,
        Field(
            alias='minThreshold',
            description='The lowest percents of a value after which resource can be rebalanced back.',
            ge=0,
            le=100,
        ),
    ]

    max_threshold: Annotated[
        float,
        Field(
            alias='maxThreshold',
            description='The highest percents of a value after which resource have be rebalanced.',
            ge=0,
            le=100,
        ),
    ]

    min_timeout: Annotated[
        float,
        Field(
            alias='minTimeout',
            description='The timeout in seconds. Fraction of value specifies milliseconds',
            gt=0,
            examples=[
                0.5,
                100,
            ],
        ),
    ]


class AlertRulePercentsOfDisk(AlertRulePercents):
    """
    Information about the threshold for disk with names.
    """
    name: Annotated[
        str,
        Field(
            title='Name of partition',
            alias='name',
        ),
    ]


class AlertRulePoints(BaseModel):
    """
    Information about the threshold in points.

    Points can be DMIPs, bytes, etc.
    """

    min_threshold: Annotated[
        int,
        Field(
            alias='minThreshold',
            description='The lowest points (DMIPs, Bytes, etc) of a value after which resource can be rebalanced back.',
            ge=0,
        ),
    ]

    max_threshold: Annotated[
        int,
        Field(
            alias='maxThreshold',
            description='The highest points of a value after which resource have be rebalanced.',
            ge=0,
        ),
    ]

    min_timeout: Annotated[
        float,
        Field(
            alias='minTimeout',
            description='The timeout in seconds. Fraction of value specifies milliseconds',
            gt=0,
            examples=[
                0.5,
                100,
            ],
        ),
    ]


class ResourceRatiosInfo(BaseModel):

    cpu: Annotated[
        float,
        Field(
            default=None,
            alias='cpu',
            description='The CPU ratio in percent.',
        ),
    ]

    ram: Annotated[
        float,
        Field(
            default=None,
            alias='ram',
            description='The memory (RAM) ratio in percent.',
        ),
    ]

    storage: Annotated[
        float,
        Field(
            default=None,
            alias='storage',
            description='The storage ratio in percent.',
        ),
    ]

    state: Annotated[
        float,
        Field(
            default=None,
            alias='state',
            description='Requested size of the "state" partition (in percents of its capacity).',
        ),
    ]


class AlertRules(BaseModel):
    cpu: Annotated[
        AlertRulePercents,
        Field(
            default=None,
            alias='cpu',
            description='The CPU thresholds.',
        ),
    ]

    ram: Annotated[
        AlertRulePercents,
        Field(
            default=None,
            alias='ram',
            description='The memory thresholds.',
        ),
    ]

    partitions: Annotated[
        Optional[list[AlertRulePercentsOfDisk]],
        Field(
            default=None,
            alias='partitions',
            description='The list of thresholds partitions.',
        ),
    ]

    download: Annotated[
        AlertRulePoints,
        Field(
            default=None,
            alias='download',
            description='The incoming to the unit traffic thresholds (in bytes).',
        )
    ]

    upload: Annotated[
        AlertRulePoints,
        Field(
            default=None,
            alias='upload',
            description='The outgoing from the unit traffic thresholds (in bytes).',
        )
    ]


class ResourceInfo(BaseModel):

    name: Annotated[
        str,
        Field(
            alias='name',
            description='The name of the resource.',
        ),
    ]

    groups: Annotated[
        list[str],
        Field(
            default=None,
            alias='groups',
            description='The group names for the resource.',
        ),
    ]

    mounts: Annotated[
        list[AosFileSystemMount],
        Field(
            default=None,
            alias='mounts',
            description='The mounts list available for running services.',
        ),
    ]

    envs: Annotated[
        list[str],
        Field(
            default=None,
            alias='envs',
            description='The list of environment variables.',
        ),
    ]

    hosts: Annotated[
        list[AosHostRecord],
        Field(
            default=None,
            alias='hosts',
            description='The list of hostnames.',
        ),
    ]


class NodeConfig(BaseModel):
    """Configuration parameters for a unit's node."""

    node_type: TypeNodeTypeMandatory
    node_id: TypeNodeIdOptional

    alert_rules: Annotated[
        AlertRules,
        Field(
            default=None,
            alias='alertRules',
            description='The default thresholds for services running on the node.',
        ),
    ]

    resource_ratios: Annotated[
        ResourceRatiosInfo,
        Field(
            alias='resourceRatios',
            default=None,
            description='The requested ratio for each resource.',
        ),
    ]

    devices: Annotated[
        list[AosDeviceInfo],
        Field(
            default=None,
            alias='devices',
            description='The devices list available for running services.',
        ),
    ]

    resources: Annotated[
        list[ResourceInfo],
        Field(
            default=None,
            alias='resources',
            description='The list of resources available for running services.',
        ),
    ]

    labels: Annotated[
        list[str],
        Field(
            default=None,
            description='The list of labels for this node.',
        ),
    ]

    priority: Annotated[
        int,
        Field(
            alias='priority',
            description='The priority of the node for deploying services.',
            ge=0,
            lt=(2**32) - 1,  # noqa: WPS432
        ),
    ]


class UnitConfig(BaseModel):
    """Configuration parameters for a unit."""

    format_version: Annotated[
        str | int,
        Field(
            alias='formatVersion',
            description='Version of the configuration object (this object).',
        ),
    ]

    version: TypeVersionMandatory

    nodes: Annotated[
        list[NodeConfig],
        Field(
            description='The list of node configurations.',
        ),
    ]
