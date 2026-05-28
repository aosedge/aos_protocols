#
#  Copyright (c) 2026 EPAM Systems Inc.
#
from typing import Annotated, List, Optional

from pydantic import BaseModel, Field

from .common import MonitoringConfig


class CMMonitoringConfig(MonitoringConfig):
    """Node monitoring configuration for the CM."""

    send_period: Annotated[
        Optional[str],
        Field(
            alias='sendPeriod',
            default='1m',
            description="""\
Interval for forwarding collected monitoring data to the cloud. Default: 1m.
Format: duration string (e.g. "1m", "5m", "30s").""",
            examples=['1m', '5m', '30s'],
        ),
    ]


class NodeInfoProviderConfig(BaseModel):
    """Node info provider subsystem configuration."""

    sm_connection_timeout: Annotated[
        Optional[str],
        Field(
            alias='smConnectionTimeout',
            default='1m',
            description="""\
Timeout waiting for SM nodes to connect during node info collection. Default: 1m.
Format: duration string (e.g. "1m", "5m", "30s").""",
            examples=['1m', '5m', '30s'],
        ),
    ]


class AlertsConfig(BaseModel):
    """Alerts subsystem configuration."""

    send_period: Annotated[
        Optional[str],
        Field(
            alias='sendPeriod',
            default='10s',
            description="""\
Interval for forwarding accumulated alert batches to the cloud. Default: 10s.
Format: duration string (e.g. "10s", "30s", "1m").""",
            examples=['10s', '30s', '1m'],
        ),
    ]


class CMImageManagerConfig(BaseModel):
    """Image manager subsystem configuration."""

    install_path: Annotated[
        Optional[str],
        Field(
            alias='installPath',
            default=None,
            description='Directory where deployable item OCI images are installed. Defaults to {workingDir}/install.',
        ),
    ]

    download_path: Annotated[
        Optional[str],
        Field(
            alias='downloadPath',
            default=None,
            description='Staging directory for deployable item image downloads. Defaults to {workingDir}/download.',
        ),
    ]

    update_item_ttl: Annotated[
        Optional[str],
        Field(
            alias='updateItemTtl',
            default='30d',
            description="""\
TTL for pending update items before they are considered outdated. Default: 30d.
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
Format: duration string (e.g. "24h", "12h", "48h").""",
            examples=['24h', '12h', '48h'],
        ),
    ]


class LauncherConfig(BaseModel):
    """Deployable item launcher subsystem configuration."""

    nodes_connection_timeout: Annotated[
        Optional[str],
        Field(
            alias='nodesConnectionTimeout',
            default='10m',
            description="""\
Timeout for all SM nodes to connect before the launcher starts scheduling deployable items. Default: 10m.
Format: duration string (e.g. "10m", "5m", "1m").""",
            examples=['10m', '5m', '1m'],
        ),
    ]

    instance_ttl: Annotated[
        Optional[str],
        Field(
            alias='instanceTtl',
            default='30d',
            description="""\
TTL for cached deployable item instance metadata. Default: 30d.
Format: duration string (e.g. "30d", "7d", "1d").""",
            examples=['30d', '7d', '1d'],
        ),
    ]

    check_override_env_vars_period: Annotated[
        Optional[str],
        Field(
            alias='checkOverrideEnvVarsPeriod',
            default='1m',
            description="""\
Interval for polling overridden environment variable changes. Default: 1m.
Format: duration string (e.g. "1m", "5m", "30s").""",
            examples=['1m', '5m', '30s'],
        ),
    ]


class MigrationConfig(BaseModel):
    """Database migration configuration."""

    migration_path: Annotated[
        Optional[str],
        Field(
            alias='migrationPath',
            default='/usr/share/aos/communicationmanager/migration',
            description='Directory containing migration SQL scripts. Default: /usr/share/aos/communicationmanager/migration.',
        ),
    ]

    merged_migration_path: Annotated[
        Optional[str],
        Field(
            alias='mergedMigrationPath',
            default=None,
            description='Directory for merged migration scripts. Defaults to {workingDir}/migration.',
        ),
    ]


class CMConfig(BaseModel):
    """
    Communication Manager (CM) configuration schema.

    This schema describes the JSON configuration file for the Aos Communication Manager,
    typically located at /etc/aos/cm.cfg .
    """

    working_dir: Annotated[
        str,
        Field(
            alias='workingDir',
            description='Working directory for all CM runtime data (images, databases, states, etc.).',
        ),
    ]

    ca_cert: Annotated[
        str,
        Field(
            alias='caCert',
            description='Path to the CA certificate file used for mutual TLS connections.',
        ),
    ]

    service_discovery_url: Annotated[
        str,
        Field(
            alias='serviceDiscoveryUrl',
            description='URL of the cloud service discovery endpoint.',
            examples=['www.aos.com'],
        ),
    ]

    iam_public_server_url: Annotated[
        str,
        Field(
            alias='iamPublicServerUrl',
            description='URL of the IAM public gRPC server.',
            examples=['localhost:8090'],
        ),
    ]

    iam_protected_server_url: Annotated[
        str,
        Field(
            alias='iamProtectedServerUrl',
            description='URL of the IAM protected gRPC server used for certificate operations.',
            examples=['localhost:8089'],
        ),
    ]

    cm_server_url: Annotated[
        str,
        Field(
            alias='cmServerUrl',
            description='URL of the CM gRPC server (self-hosted endpoint listened to by SM nodes).',
            examples=['localhost:8094'],
        ),
    ]

    file_server_url: Annotated[
        Optional[str],
        Field(
            alias='fileServerUrl',
            default=None,
            description='URL of the file server for downloading deployable item OCI image archives.',
            examples=['localhost:8080'],
        ),
    ]

    dns_ip: Annotated[
        Optional[str],
        Field(
            alias='dnsIp',
            default=None,
            description='Address (host:port) of the internal DNS server managed by the CM.',
            examples=['0.0.0.0:5353', '127.0.0.1:5353'],
        ),
    ]

    cert_storage: Annotated[
        Optional[str],
        Field(
            alias='certStorage',
            default='/var/aos/crypt/cm/',
            description='Certificate storage identifier for CM TLS credentials. Default: /var/aos/crypt/cm/.',
        ),
    ]

    storage_dir: Annotated[
        Optional[str],
        Field(
            alias='storageDir',
            default=None,
            description='Directory for deployable item persistent storage volumes. Defaults to {workingDir}/storages.',
        ),
    ]

    state_dir: Annotated[
        Optional[str],
        Field(
            alias='stateDir',
            default=None,
            description='Directory for deployable item state data. Defaults to {workingDir}/states.',
        ),
    ]

    unit_config_file: Annotated[
        Optional[str],
        Field(
            alias='unitConfigFile',
            default=None,
            description='Path to the unit configuration file. Defaults to {workingDir}/aos_unit.cfg.',
        ),
    ]

    dns_storage_path: Annotated[
        Optional[str],
        Field(
            alias='dnsStoragePath',
            default='/var/aos/dns',
            description='Directory for DNS server persistent data. Default: /var/aos/dns.',
        ),
    ]

    override_service_discovery_url: Annotated[
        Optional[str],
        Field(
            alias='overrideServiceDiscoveryUrl',
            default=None,
            description='Override URL for service discovery; replaces serviceDiscoveryUrl in test/dev environments.',
        ),
    ]

    cloud_message_log: Annotated[
        Optional[str],
        Field(
            alias='cloudMessageLog',
            default=None,
            description='Path to a file for logging raw cloud protocol messages (for debugging).',
        ),
    ]

    unit_status_send_timeout: Annotated[
        Optional[str],
        Field(
            alias='unitStatusSendTimeout',
            default='10s',
            description="""\
Timeout for sending unit status updates to the cloud. Default: 10s.
Format: duration string (e.g. "10s", "30s", "1m").""",
            examples=['10s', '30s', '1m'],
        ),
    ]

    cloud_response_wait_timeout: Annotated[
        Optional[str],
        Field(
            alias='cloudResponseWaitTimeout',
            default='10s',
            description="""\
Timeout waiting for a cloud response after sending a request. Default: 10s.
Format: duration string (e.g. "10s", "30s", "1m").""",
            examples=['10s', '30s', '1m'],
        ),
    ]

    monitoring: Annotated[
        Optional[CMMonitoringConfig],
        Field(
            alias='monitoring',
            default=None,
            description='Node monitoring subsystem configuration.',
        ),
    ]

    node_info_provider: Annotated[
        Optional[NodeInfoProviderConfig],
        Field(
            alias='nodeInfoProvider',
            default=None,
            description='Node info provider subsystem configuration.',
        ),
    ]

    alerts: Annotated[
        Optional[AlertsConfig],
        Field(
            alias='alerts',
            default=None,
            description='Alerts subsystem configuration.',
        ),
    ]

    image_manager: Annotated[
        Optional[CMImageManagerConfig],
        Field(
            alias='imageManager',
            default=None,
            description='Image manager subsystem configuration.',
        ),
    ]

    launcher: Annotated[
        Optional[LauncherConfig],
        Field(
            alias='launcher',
            default=None,
            description='Deployable item launcher subsystem configuration.',
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
