#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from datetime import timedelta
from typing import Annotated, Literal, Optional, List, Dict

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.v7.common import AosOsInfo, AosArchInfo, AosIdentity


class AosImage(BaseModel):

    source_folder: Annotated[
        str,
        Field(
            alias='sourceFolder',
            description='Source folder for the image.',
        ),
    ]

    os_info: Annotated[
        AosOsInfo,
        Field(
            default=AosOsInfo(os='Linux'),
            alias='osInfo',
            description='OS information of the image.',
        ),
    ] = AosOsInfo(os='Linux')

    arch_info: Annotated[
        AosArchInfo,
        Field(
            alias='archInfo',
            description='Architecture information of the image.',
        ),
    ]

    env: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            alias='env',
            description='Environment variables for the image.',
        ),
    ] = None

    working_dir: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='workingDir',
            description='Working directory for the image.',
        ),
    ] = None

    cmd: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='cmd',
            description='Command line for the image.',
        ),
    ] = None


class AosRunParameters(BaseModel):
    start_interval: Annotated[
        Optional[timedelta],
        Field(
            alias='startInterval',
            default=None,
            description='The duration in ISO8601 format to wait service start.',
            examples=['PT10S', 'PT1M'],
        ),
    ]

    start_burst: Annotated[
        Optional[int],
        Field(
            alias='startBurst',
            default=None,
            description="""\
    Service which are started more than burst times within an interval time span are not permitted to start any more.
    Use `startInterval` to configure the checking interval and `startBurst`
    to configure how many starts per interval are allowed.""",
            examples=[3, 10],
        ),
    ]

    restart_interval: Annotated[
        Optional[timedelta],
        Field(
            alias='restartInterval',
            default=None,
            description='The duration in ISO8601 format to wait before service restart.',
            examples=['PT1S', 'PT1M'],
        ),
    ]


class AosResourceAccess(BaseModel):
    name: Annotated[
        str,
        Field(
            alias='name',
            description="The name of the systems device.",
            examples=['camera0', 'mic0'],
        ),
    ]

    mode: Annotated[
        Literal['w', 'rw', 'w', 'm', 'rwm'],
        Field(
            default='r',
            description='The needed access permissions for the resource.',
            examples=['r', 'rw', 'w'],
        ),
    ] = 'r'


class AosAlertRulePoints(BaseModel):
    """Schema alert triggering procedure."""

    min_timeout: Annotated[
        Optional[timedelta],
        Field(
            alias='minTimeout',
            description='The duration in ISO8601 for a time window to check alert rule.',
            examples=['PT10S', 'PT1M'],
        ),
    ]

    min_threshold: Annotated[
        Optional[int],
        Field(
            alias='minThreshold',
            description='The minimum threshold to stop alert.',
        ),
    ]

    max_threshold: Annotated[
        Optional[int],
        Field(
            alias='maxThreshold',
            description='The maximum threshold value to start alert.',
        ),
    ]


class AosAlertRulePercents(BaseModel):
    """Schema alert triggering procedure in percents."""

    min_timeout: Annotated[
        Optional[timedelta],
        Field(
            alias='minTimeout',
            description='The duration in ISO8601 for a time window to check alert rule.',
            examples=['PT10S', 'PT1M'],
        ),
    ]

    min_threshold: Annotated[
        Optional[float],
        Field(
            alias='minThreshold',
            ge=0,
            le=100,
            description='The minimum threshold to stop alert.',
        ),
    ]

    max_threshold: Annotated[
        Optional[float],
        Field(
            alias='maxThreshold',
            ge=0,
            le=100,
            description='The maximum threshold value to start alert.',
        ),
    ]


class AosAlertRules(BaseModel):
    """Schema for all possible alert rules."""

    ram: Annotated[
        Optional[AosAlertRulePercents],
        Field(
            alias='ram',
            default=None,
            description='RAM alert settings.',
        ),
    ] = None

    cpu: Annotated[
        Optional[AosAlertRulePercents],
        Field(
            alias='cpu',
            default=None,
            description='CPU alert settings.',
        ),
    ] = None

    storage: Annotated[
        Optional[AosAlertRulePercents],
        Field(
            alias='storage',
            default=None,
            description='Storage alert settings.',
        ),
    ] = None

    upload: Annotated[
        Optional[AosAlertRulePoints],
        Field(
            alias='upload',
            default=None,
            description='Upload alert settings.',
        ),
    ] = None

    download: Annotated[
        Optional[AosAlertRulePoints],
        Field(
            alias='download',
            default=None,
            description='Download alert settings.',
        ),
    ] = None


class AosQuotas(BaseModel):
    """Schema for possible quotas for an Aos item."""

    cpu_limit: Annotated[
        Optional[int],
        Field(
            alias='cpuLimit',
            default=None,
            description='CPU limit in DMIPs',
        ),
    ] = None

    ram_limit: Annotated[
        Optional[int],
        Field(
            alias='ramLimit',
            default=None,
            description='RAM limit in bytes',
        ),
    ] = None

    storage_limit: Annotated[
        Optional[int],
        Field(
            alias='storageLimit',
            default=None,
            description='Storage limit in bytes',
        ),
    ] = None

    state_limit: Annotated[
        Optional[int],
        Field(
            alias='stateLimit',
            default=None,
            description='State limit in bytes',
        ),
    ] = None

    tmp_limit: Annotated[
        Optional[int],
        Field(
            alias='tmpLimit',
            default=None,
            description='Temporary storage limit in bytes',
        ),
    ] = None

    upload_speed: Annotated[
        Optional[int],
        Field(
            alias='uploadSpeed',
            default=None,
            description='Upload limit in bits per second',
        ),
    ] = None

    download_speed: Annotated[
        Optional[int],
        Field(
            alias='downloadSpeed',
            default=None,
            description='Upload limit in bits per second',
        ),
    ] = None

    files_limit: Annotated[
        Optional[int],
        Field(
            alias='noFileLimit',
            default=None,
            description='Limit of opened files',
        ),
    ] = None

    pids_limit: Annotated[
        Optional[int],
        Field(
            alias='pidsLimit',
            default=None,
            description='Limit of PIDs',
        ),
    ] = None


class AosInstancesInfo(BaseModel):
    """Schema for instances info."""

    min_instances: Annotated[
        int,
        Field(
            alias='minInstances',
            description='Minimum number of instances.',
            default=1,
            gt=1,
            le=100,
        ),
    ] = 1

    priority: Annotated[
        int,
        Field(
            alias='priority',
            description='Priority of the instances.',
            default=0,
            ge=0,
        ),
    ] = 0

    labels: Annotated[
        Optional[list[str]],
        Field(
            alias='labels',
            description='Labels of the instances.',
            default=None,
        ),
    ] = None


class AosUpdateItemConfiguration(BaseModel):

    env: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            alias='env',
            description='Environment variables for the image.',
        ),
    ] = None

    working_dir: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='workingDir',
            description='Working directory for the image.',
        ),
    ] = None

    instances: Annotated[
        Optional[AosInstancesInfo],
        Field(
            default=None,
            alias='instances',
            description='Instances info.',
        ),
    ] = None

    cmd: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='cmd',
            description='Command line for the image.',
        ),
    ] = None

    skip_resource_limits: Annotated[
        bool,
        Field(
            alias='skipResourceLimits',
            default=False,
            description='Use resource limits or not in pre-release versions.',
        ),
    ] = False

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
    ] = 'enabled'

    base_layer_is_node_rootfs: Annotated[
        Optional[bool],
        Field(
            alias='baseLayerIsNodeRootfs',
            default=True,
            description='Whether the base layer is the node rootfs or not.',
        ),
    ] = True

    hostname: Annotated[
        Optional[str],
        Field(
            alias='hostname',
            default=None,
            description='The hostname of the Aos service. The FQDN is {hostname].{service_provider}.',
        ),
    ] = None

    exposed_ports: Annotated[
        Optional[list[int | str]],
        Field(
            alias='exposedPorts',
            default=None,
            description='List of exposed ports in format {port}/[tcp|udp].',
            examples=[8080, 8081, '53/udp'],
        ),
    ] = None

    runtimes: Annotated[
        list[AosIdentity],
        Field(
            alias='runtimes',
            default=[AosIdentity(codename='runc', type='runtime'), AosIdentity(codename='crun', type='runtime')],
            description='Aos service allowed runner types. Absense means ["runc", "crun"].',
        ),
    ]

    run_parameters: Annotated[
        Optional[AosRunParameters],
        Field(
            alias='runParameters',
            default=None,
            description='Run parameters for the Aos item.',
        ),
    ] = None

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
    ] = None

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
        )
    ] = None

    allowed_connections: Annotated[
        Optional[list[str]],
        Field(
            alias='allowedConnections',
            default=None,
            description="""\
    List of allowed network connections.
    Format of connection string: {fqdn}/[port|port_range]/[tcp|udp]""",
            examples=[
                'hello-world/8087:8088/tcp',
                'hello-world/1515/udp',
            ]
        ),
    ] = None

    quotas: Annotated[
        Optional[AosQuotas],
        Field(
            alias='quotas',
            default=None,
            description='Quotas for the service.'
        ),
    ]

    alert_rules: Annotated[
        Optional[AosAlertRules],
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
            description='Permissions to access resources.',
            examples=[{'vis': {'Signal.Doors.*': 'rw', 'Attributes.Vehicle.Vin': 'r'}}],
        ),
    ]


class AosDependency(BaseModel):

    identity: Annotated[
        AosIdentity,
        Field(
            alias='identity',
            description='Identity of the AOS object.',
        ),
    ]

    versions: Annotated[
        str,
        Field(
            alias='versions',
            description='Versions of the AOS object.',
            examples=['>=1.0.0,<2.0.0', '1.2.3'],
        ),
    ]

    includePrerelease: Annotated[
        bool,
        Field(
            alias='includePreRelease',
            description='Include pre-release versions.',
            default=False,
        ),
    ] = False

    condition: Annotated[
        Literal[
            'started',
            'healthy',
            'completed',
            'before',
            'after',
        ],
        Field(
            default='completed',
            alias='condition',
            description='Condition for dependency of the AOS object.',
        ),
    ] = 'completed'



class AosUpdateItem(BaseModel):

    identity: Annotated[
        AosIdentity,
        Field(
            alias='identity',
            description='Identity of the update item.',
        ),
    ]

    version: Annotated[
        str,
        Field(
            alias='version',
            description='Version in SemVer format of the update item.',
        ),
    ]

    source_folder: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='sourceFolder',
            description='Source folder for the item. If absent, codename from identity will be used.',
        ),
    ] = None

    images: Annotated[
        list[AosImage],
        Field(
            alias='images',
            description='List of images for different architectures.',
            min_length=1
        ),
    ]

    configuration: Annotated[
        Optional[AosUpdateItemConfiguration],
        Field(
            default=None,
            alias='configuration',
            description='Configuration of the update item.',
        ),
    ] = None

    dependencies: Annotated[
        Optional[list[AosDependency]],
        Field(
            default=None,
            alias='dependencies',
            description='List of the update item dependencies.',
        ),
    ]


class RequestedResources(BaseModel):
    """
    Schema for requested resources.
    """

    cpu: Annotated[
        Optional[int],
        Field(
            alias='cpu',
            default=None,
            description='CPU requested resource (against cpuLimit)',
        ),
    ]

    ram: Annotated[
        Optional[int],
        Field(
            alias='ram',
            default=None,
            description='RAM requested resource (against ramLimit)',
        ),
    ]

    storage: Annotated[
        Optional[int],
        Field(
            alias='storage',
            default=None,
            description='Storage requested resource (against storageLimit)',
        ),
    ]

    state: Annotated[
        Optional[int],
        Field(
            alias='state',
            default=None,
            description='State requested resource (against stateLimit)',
        ),
    ]


class RunParameters(BaseModel):
    """Schema for startup parameters."""

    start_interval: Annotated[
        Optional[timedelta],
        Field(
            alias='startInterval',
            default=None,
            description='The duration in ISO8601 format to wait service start.',
            examples=['PT10S', 'PT1M'],
        ),
    ]

    start_burst: Annotated[
        Optional[int],
        Field(
            alias='startBurst',
            default=None,
            description="""\
Service which are started more than burst times within an interval time span are not permitted to start any more.
Use `startInterval` to configure the checking interval and `startBurst`
to configure how many starts per interval are allowed.""",
            examples=[3, 10],
        ),
    ]

    restart_interval: Annotated[
        Optional[timedelta],
        Field(
            alias='restartInterval',
            default=None,
            description='The duration in ISO8601 format to wait before service restart.',
            examples=['PT1S', 'PT1M'],
        ),
    ]


class ServiceQuotas(BaseModel):
    """Schema for possible quotas for a service."""

    cpu_limit: Annotated[
        Optional[int],
        Field(
            alias='cpuLimit',
            default=None,
            description='CPU limit in percents',
        ),
    ]
    cpu_dmips_limit: Annotated[
        Optional[int],
        Field(
            alias='cpuDmipsLimit',
            default=None,
            description='CPU limit in DMIPs',
        ),
    ]

    ram_limit: Annotated[
        Optional[int],
        Field(
            alias='ramLimit',
            default=None,
            description='RAM limit in bytes',
        ),
    ]

    storage_limit: Annotated[
        Optional[int],
        Field(
            alias='storageLimit',
            default=None,
            description='Storage limit in bytes',
        ),
    ]

    state_limit: Annotated[
        Optional[int],
        Field(
            alias='stateLimit',
            default=None,
            description='State limit in bytes',
        ),
    ]

    tmp_limit: Annotated[
        Optional[int],
        Field(
            alias='tmpLimit',
            default=None,
            description='Temporary storage limit in bytes',
        ),
    ]

    upload_speed: Annotated[
        Optional[int],
        Field(
            alias='uploadSpeed',
            default=None,
            description='Upload limit in bytes per second',
        ),
    ]

    download_speed: Annotated[
        Optional[int],
        Field(
            alias='downloadSpeed',
            default=None,
            description='Upload limit in bytes per second',
        ),
    ]

    files_limit: Annotated[
        Optional[int],
        Field(
            alias='noFileLimit',
            default=None,
            description='Limit of opened files',
        ),
    ]

    pids_limit: Annotated[
        Optional[int],
        Field(
            alias='pidsLimit',
            default=None,
            description='Limit of PIDs',
        ),
    ]
