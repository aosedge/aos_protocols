#
#  Copyright (c) 2018-2026 EPAM Systems Inc.
#
from datetime import datetime, timedelta
from typing import Annotated, Dict, Literal, Optional

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.v7.common import AosIdentity

from .aos_types import (
    AosResourceAccess,
    AosAlertRules,
    RequestedResources,
    RunParameters,
    ServiceQuotas,
)


class AosConfigSchemaV2(BaseModel):
    """
    Aos deployable item config schema.

    This schema describes the specification of the
     `application/vnd.aos.item.config.v1+json` layer in a deployable item.
    """

    created: Annotated[
        datetime,
        Field(
            alias='created',
            description='Timestamp when Aos service was created.',
        ),
    ]

    author: Annotated[
        Optional[str],
        Field(
            alias='author',
            default=None,
            description='Aos service author.',
        ),
    ]

    skip_resource_limits: Annotated[
        Optional[bool],
        Field(
            alias='skipResourceLimits',
            default=None,
            description='Use resource limits or not in Pre-release versions.',
        ),
    ]

    balancing_policy: Annotated[
        Literal[
            'enabled',
            'disabled',
        ],
        Field(
            alias='balancingPolicy',
            default='enabled',
            description='Balancing type. `disabled` means total prohibition from balancing to other nodes.',
        ),
    ]

    hostname: Annotated[
        Optional[str],
        Field(
            alias='hostname',
            default=None,
            description='The hostname of the Aos service. The FQDN is {hostname].{service_provider}.',
        ),
    ]

    runner: Annotated[  # Deprecated
        Optional[Literal['runc', 'crun', 'xrun']],
        Field(
            alias='runner',
            default='crun',
            description='Aos service allowed runner type. Use for backward compatibility with previous version of Aos',
        ),
    ]

    runners: Annotated[
        Optional[list[Literal['runc', 'crun', 'xrun']]],
        Field(
            alias='runners',
            default=['runc', 'crun'],
            description='Aos service allowed runner types. Absense means ["runc", "crun"].',
        ),
    ]

    runtimes: Annotated[
        Optional[list[AosIdentity]],
        Field(
            alias='runtimes',
            default=None,
            description='Aos service allowed runtimes. Absense means all runtimes.',
        ),
    ] = None

    run_parameters: Annotated[
        Optional[RunParameters],
        Field(
            alias='runParameters',
            default=None,
            description='Run parameters for the Aos service.',
        ),
    ]

    offline_ttl: Annotated[
        Optional[timedelta],
        Field(
            alias='offlineTTL',
            default=None,
            description="""\
TTL (allowed time) to run service when unit in offline mode.
If value is absent service will live on an unit forever.
Format: ISO8601 duration.""",
            examples=['PT1M', 'PT7D'],
        ),
    ]

    resources: Annotated[
        Optional[list[AosResourceAccess]],
        Field(
            alias='resources',
            default=None,
            description='List of needed resources.',
            examples=[
                AosResourceAccess(name='bluetooth', mode='rw'),
                AosResourceAccess(name='system-dbus', mode='rw'),
                AosResourceAccess(name='camera0'),
            ],
        ),
    ] = None

    allowed_connections: Annotated[
        Optional[dict],
        Field(
            alias='allowedConnections',
            default=None,
            description="""\
List of allowed network connections.
Format of connection string: {service_uid}/[port|port_range]/[tcp|udp]""",
            examples=[
                '9931560c-be75-4f60-9abf-08297d905332/8087:8088/tcp',
                '9931560c-be75-4f60-9abf-08297d905332/1515/udp',
            ],
        ),
    ]

    quotas: Annotated[
        Optional[ServiceQuotas],
        Field(
            alias='quotas',
            default=None,
            description='Quotas for the service.',
        ),
    ]

    requested_resources: Annotated[
        Optional[RequestedResources],
        Field(
            alias='requestedResources',
            default=None,
            description='Requested Resources (CPU, RAM and Storage).',
        ),
    ]

    alert_rules: Annotated[
        Optional[AosAlertRules],
        Field(
            alias='alertRules',
            default=None,
            description='Alert rules for the service.',
        ),
    ]

    permissions: Annotated[  # noqa: TAE002
        Optional[Dict[str, Dict[str, Literal['r', 'rw', 'w']]]],
        Field(
            alias='permissions',
            default=None,
            description='Service permissions to access resources.',
            examples=[{'vis': {'Signal.Doors.*': 'rw', 'Attributes.Vehicle.Vin': 'r'}}],
        ),
    ]

    sysctl: Annotated[
        Optional[Dict[str, str]],
        Field(
            alias='sysctl',
            default=None,
            description='Kernel parameters to be modified at runtime for the container.',
            examples=[
                {
                    'net.ipv4.ip_forward': '1',
                    'net.core.somaxconn': '256',
                },
            ],
        ),
    ]
