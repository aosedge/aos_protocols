#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from datetime import datetime, timedelta
from typing import Annotated, Optional, Literal, Dict, List

from pydantic import BaseModel, Field

from cloud_common.schemas.service_config.aos_types import (
    UnitDevice,
    RunParameters,
    ServiceQuotas,
    AlertRules,
    RequestedResources, AosDependency,
)


class AosConfigSchema(BaseModel):
    """
    Aos service config schema.

    This schema describes the specification of the `aosService` layer in a service.
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
            description='Use resource limits or not in pre-release versions.',
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
            description='Balancing type. `disabled` means total prohibition from balancing to other nodes.`',
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

    runners: Annotated[
        Optional[list[Literal['runc', 'crun', 'xrun']]],
        Field(
            alias='runners',
            default=None,
            description='Aos service allowed runner types. Absense means ["runc", "crun"].',
        ),
    ]

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
            examples=['PT1M', 'PT7D']
        ),
    ]

    devices: Annotated[
        Optional[UnitDevice],
        Field(
            alias='devices',
            default=None,
            description='List of needed or requested devices.'
        ),
    ]

    resources: Annotated[
        Optional[list[str]],
        Field(
            alias='resources',
            default=None,
            description='List of needed resources.',
            examples=['bluetooth', 'system-dbus'],
        )
    ]

    allowed_connections: Annotated[
        Optional[list[dict]],
        Field(
            alias='allowedConnections',
            default=None,
            description="""\
List of allowed network connections.
Format of connection string: {service_uid}/[port|port_range]/[tcp|udp]""",
            examples=[
                '9931560c-be75-4f60-9abf-08297d905332/8087:8088/tcp',
                '9931560c-be75-4f60-9abf-08297d905332/1515/udp',
            ]
        ),
    ]

    quotas: Annotated[
        Optional[ServiceQuotas],
        Field(
            alias='quotas',
            default=None,
            description='Quotas for the service.'
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
        Optional[AlertRules],
        Field(
            alias='alertRules',
            default=None,
            description='Alert rules for the service.'
        ),
    ]

    permissions: Annotated[
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
            ]
        ),
    ]

    dependencies: Annotated[
        Optional[List[AosDependency]],
        Field(
            alias='dependencies',
            default=None,
            description='List of dependencies.',
        ),
    ] = None
