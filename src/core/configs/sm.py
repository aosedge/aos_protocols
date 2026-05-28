#
#  Copyright (c) 2026 EPAM Systems Inc.
#
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field

from .common import MonitoringConfig


class ImageManagerConfig(BaseModel):
    """Image manager subsystem configuration."""

    image_path: Annotated[
        Optional[str],
        Field(
            alias='imagePath',
            default=None,
            description='Path to store deployable item images. Defaults to {workingDir}/images.',
        ),
    ]

    images_part_limit: Annotated[
        Optional[int],
        Field(
            alias='imagesPartLimit',
            default=0,
            description='Maximum number of image parts retained. 0 means unlimited.',
        ),
    ]

    update_item_ttl: Annotated[
        Optional[str],
        Field(
            alias='updateItemTtl',
            default='30d',
            description="""\
Time-to-live for pending update items before they are considered outdated. Default: 30d.
Format: duration string (e.g. "30d", "7d", "24h").""",
            examples=['30d', '7d', '24h'],
        ),
    ]

    remove_outdated_period: Annotated[
        Optional[str],
        Field(
            alias='removeOutdatedPeriod',
            default='24h',
            description="""\
Period between removal passes for outdated images. Default: 24h.
Format: duration string (e.g. "24h", "12h", "1d").""",
            examples=['24h', '12h', '48h'],
        ),
    ]


class LoggingConfig(BaseModel):
    """Log provider subsystem configuration."""

    max_part_size: Annotated[
        Optional[int],
        Field(
            alias='maxPartSize',
            default=None,
            description='Maximum size in bytes of a single log part. Defaults to the compiled-in cLogContentLen.',
            examples=[1024, 65536],
        ),
    ]

    max_part_count: Annotated[
        Optional[int],
        Field(
            alias='maxPartCount',
            default=80,
            description='Maximum number of log parts kept per request. Default: 80.',
        ),
    ]


class JournalAlertsConfig(BaseModel):
    """Systemd journal alerts subsystem configuration."""

    filter: Annotated[
        Optional[List[str]],
        Field(
            alias='filter',
            default=None,
            description='List of regular expressions matched against journal log entries to generate alerts.',
            examples=[['error', 'critical', 'panic']],
        ),
    ]

    service_alert_priority: Annotated[
        Optional[int],
        Field(
            alias='serviceAlertPriority',
            default=4,
            ge=0,
            le=7,
            description="""\
Minimum syslog priority level for service-specific journal alerts (0=emerg … 7=debug).
Values outside [0, 7] are reset to the default. Default: 4 (warning).""",
        ),
    ]

    system_alert_priority: Annotated[
        Optional[int],
        Field(
            alias='systemAlertPriority',
            default=3,
            ge=0,
            le=7,
            description="""\
Minimum syslog priority level for system-wide journal alerts (0=emerg … 7=debug).
Values outside [0, 7] are reset to the default. Default: 3 (err).""",
        ),
    ]


class MigrationConfig(BaseModel):
    """Database migration configuration."""

    migration_path: Annotated[
        Optional[str],
        Field(
            alias='migrationPath',
            default='/usr/share/aos/servicemanager/migration',
            description='Directory containing migration SQL scripts. Default: /usr/share/aos/servicemanager/migration.',
        ),
    ]

    merged_migration_path: Annotated[
        Optional[str],
        Field(
            alias='mergedMigrationPath',
            default=None,
            description='Directory for merged migration scripts. Defaults to {workingDir}/mergedMigration.',
        ),
    ]


class RuntimeConfig(BaseModel):
    """Single runtime plugin entry used by the launcher."""

    plugin: Annotated[
        str,
        Field(
            alias='plugin',
            description='Runtime plugin identifier (e.g. "container", "rootfs", "boot").',
            examples=['container', 'rootfs', 'boot'],
        ),
    ]

    type: Annotated[
        str,
        Field(
            alias='type',
            description='Runtime type name passed to the plugin (e.g. "runc", "crun", "aos-vm-rootfs").',
            examples=['runc', 'crun', 'aos-vm-rootfs', 'aos-vm-boot'],
        ),
    ]

    is_component: Annotated[
        Optional[bool],
        Field(
            alias='isComponent',
            default=False,
            description='Set to true when this runtime handles component (firmware) updates.',
        ),
    ]

    config: Annotated[
        Optional[Any],
        Field(
            alias='config',
            default=None,
            description='Plugin-specific configuration object. Passed verbatim to the runtime plugin.',
        ),
    ]


class SMConfig(BaseModel):
    """
    Service Manager (SM) configuration schema.

    This schema describes the JSON configuration file for the Aos Service Manager,
    typically located at /etc/aos/sm.cfg .
    """

    working_dir: Annotated[
        str,
        Field(
            alias='workingDir',
            description='Working directory for all SM runtime data (images, databases, etc.).',
        ),
    ]

    iam_public_server_url: Annotated[
        str,
        Field(
            alias='iamPublicServerURL',
            description='URL of the IAM public gRPC server.',
            examples=['localhost:8090'],
        ),
    ]

    ca_cert: Annotated[
        str,
        Field(
            alias='caCert',
            description='Path to the CA certificate file used for mutual TLS connections.',
        ),
    ]

    iam_protected_server_url: Annotated[
        str,
        Field(
            alias='iamProtectedServerURL',
            description='URL of the IAM protected gRPC server used for certificate operations.',
            examples=['localhost:8089'],
        ),
    ]

    cm_server_url: Annotated[
        str,
        Field(
            alias='cmServerURL',
            description='URL of the Cloud Manager (CM) gRPC server.',
            examples=['aoscm:8093'],
        ),
    ]

    cert_storage: Annotated[
        Optional[str],
        Field(
            alias='certStorage',
            default='/var/aos/crypt/sm/',
            description='Certificate storage identifier used for SM TLS credentials. Default: /var/aos/crypt/sm/.',
        ),
    ]

    cm_reconnect_timeout: Annotated[
        Optional[str],
        Field(
            alias='cmReconnectTimeout',
            default='10s',
            description="""\
Delay before retrying a dropped CM connection. Default: 10s.
Format: duration string (e.g. "10s", "1m").""",
            examples=['10s', '30s', '1m'],
        ),
    ]

    node_config_file: Annotated[
        Optional[str],
        Field(
            alias='nodeConfigFile',
            default=None,
            description='Path to the node configuration file. Defaults to {workingDir}/aos_node.cfg.',
        ),
    ]

    resources_config_file: Annotated[
        Optional[str],
        Field(
            alias='resourcesConfigFile',
            default='/etc/aos/resources.cfg',
            description='Path to the resources configuration file. Default: /etc/aos/resources.cfg.',
        ),
    ]

    monitoring: Annotated[
        Optional[MonitoringConfig],
        Field(
            alias='monitoring',
            default=None,
            description='Node monitoring subsystem configuration.',
        ),
    ]

    image_manager: Annotated[
        Optional[ImageManagerConfig],
        Field(
            alias='imageManager',
            default=None,
            description='Image manager subsystem configuration.',
        ),
    ]

    logging: Annotated[
        Optional[LoggingConfig],
        Field(
            alias='logging',
            default=None,
            description='Log provider subsystem configuration.',
        ),
    ]

    journal_alerts: Annotated[
        Optional[JournalAlertsConfig],
        Field(
            alias='journalAlerts',
            default=None,
            description='Systemd journal alerts subsystem configuration.',
        ),
    ]

    migration: Annotated[
        Optional[MigrationConfig],
        Field(
            alias='migration',
            default=None,
            description='Database migration configuration.',
        ),
    ]

    runtimes: Annotated[
        Optional[List[RuntimeConfig]],
        Field(
            alias='runtimes',
            default=None,
            description='List of runtime plugin configurations available to the launcher.',
        ),
    ]
