#
#  Copyright (c) 2026 EPAM Systems Inc.
#
from typing import Annotated, Any, Dict, List, Optional

from pydantic import BaseModel, Field


class PartitionInfoConfig(BaseModel):
    """Partition information for node storage reporting."""

    name: Annotated[
        str,
        Field(
            alias='name',
            description='Partition label reported to the cloud.',
        ),
    ]

    path: Annotated[
        str,
        Field(
            alias='path',
            description='Filesystem path of the partition.',
        ),
    ]

    types: Annotated[
        Optional[List[str]],
        Field(
            alias='types',
            default=None,
            description='List of partition type tags (e.g. generic, storages, states).',
            examples=[['generic'], ['storages', 'states']],
        ),
    ]


class NodeInfoConfig(BaseModel):
    """
    Node information reported by the IAM to the cloud.

    This section describes the hardware and software identity of the node.
    """

    node_name: Annotated[
        str,
        Field(
            alias='nodeName',
            description='Human-readable name of the node.',
        ),
    ]

    node_type: Annotated[
        str,
        Field(
            alias='nodeType',
            description='Node type identifier.',
        ),
    ]

    max_dmips: Annotated[
        int,
        Field(
            alias='maxDMIPS',
            description='Maximum CPU performance of the node in DMIPS.',
        ),
    ]

    node_id_path: Annotated[
        Optional[str],
        Field(
            alias='nodeIDPath',
            default='/etc/machine-id',
            description='Path to the file containing the unique node identifier. Default: /etc/machine-id.',
        ),
    ]

    provisioning_state_path: Annotated[
        Optional[str],
        Field(
            alias='provisioningStatePath',
            default='/var/aos/.provisionstate',
            description='Path to the provisioning state file. Default: /var/aos/.provisionstate.',
        ),
    ]

    cpu_info_path: Annotated[
        Optional[str],
        Field(
            alias='cpuInfoPath',
            default='/proc/cpuinfo',
            description='Path to the CPU information file. Default: /proc/cpuinfo.',
        ),
    ]

    mem_info_path: Annotated[
        Optional[str],
        Field(
            alias='memInfoPath',
            default='/proc/meminfo',
            description='Path to the memory information file. Default: /proc/meminfo.',
        ),
    ]

    architecture: Annotated[
        Optional[str],
        Field(
            alias='architecture',
            default=None,
            description='CPU architecture string (e.g. "amd64", "arm64"). Must be GOARCH-compatible if specified.',
        ),
    ]

    architecture_variant: Annotated[
        Optional[str],
        Field(
            alias='architectureVariant',
            default=None,
            description='CPU architecture variant (e.g. "v8", "v7l").',
        ),
    ]

    os: Annotated[
        Optional[str],
        Field(
            alias='os',
            description='Operating system name (e.g. "linux"). Must be GOOS-compatible if specified.',
            default=None,
        ),
    ]

    os_version: Annotated[
        Optional[str],
        Field(
            alias='osVersion',
            default=None,
            description='Operating system version string.',
        ),
    ]

    attrs: Annotated[
        Optional[Dict[str, str]],
        Field(
            alias='attrs',
            default=None,
            description='Arbitrary key/value attributes attached to the node and reported to the cloud.',
            examples=[{'key1': 'value1', 'key2': 'value2'}],
        ),
    ]

    partitions: Annotated[
        Optional[List[PartitionInfoConfig]],
        Field(
            alias='partitions',
            default=None,
            description='List of storage partitions whose usage is monitored and reported.',
        ),
    ]


class DatabaseMigrationConfig(BaseModel):
    """Database migration paths."""

    migration_path: Annotated[
        str,
        Field(
            alias='migrationPath',
            description='Directory containing migration SQL scripts.',
        ),
    ]

    merged_migration_path: Annotated[
        str,
        Field(
            alias='mergedMigrationPath',
            description='Directory for merged migration scripts.',
        ),
    ]


class CertModuleConfig(BaseModel):
    """Certificate module (plugin) configuration."""

    id: Annotated[
        str,
        Field(
            alias='id',
            description='Unique identifier of the certificate module.',
            examples=['cm', 'sm', 'iam'],
        ),
    ]

    plugin: Annotated[
        str,
        Field(
            alias='plugin',
            description='Certificate plugin type (e.g. "pkcs11", "swmodule").',
            examples=['pkcs11', 'swmodule'],
        ),
    ]

    algorithm: Annotated[
        str,
        Field(
            alias='algorithm',
            description='Key algorithm used by this module.',
            examples=['rsa', 'ecc'],
        ),
    ]

    max_items: Annotated[
        int,
        Field(
            alias='maxItems',
            description='Maximum number of certificate slots managed by this module.',
        ),
    ]

    extended_key_usage: Annotated[
        Optional[List[str]],
        Field(
            alias='extendedKeyUsage',
            default=None,
            description='X.509 extended key usage OIDs or short names for generated certificates.',
            examples=[['clientAuth'], ['serverAuth'], ['clientAuth', 'serverAuth']],
        ),
    ]

    alternative_names: Annotated[
        Optional[List[str]],
        Field(
            alias='alternativeNames',
            default=None,
            description='Subject alternative names (SANs) added to generated certificates.',
            examples=[['localhost', '127.0.0.1']],
        ),
    ]

    disabled: Annotated[
        Optional[bool],
        Field(
            alias='disabled',
            default=False,
            description='Set to true to disable this certificate module.',
        ),
    ]

    skip_validation: Annotated[
        Optional[bool],
        Field(
            alias='skipValidation',
            default=False,
            description='Skip certificate chain validation for this module (use in test environments only).',
        ),
    ]

    self_signed: Annotated[
        Optional[bool],
        Field(
            alias='selfSigned',
            default=False,
            description='Generate self-signed certificates instead of requesting signing from the IAM CA.',
        ),
    ]

    params: Annotated[
        Optional[Any],
        Field(
            alias='params',
            default=None,
            description='Plugin-specific parameters passed verbatim to the certificate plugin.',
        ),
    ]


class IdentifierConfig(BaseModel):
    """Identifier plugin configuration."""

    plugin: Annotated[
        str,
        Field(
            alias='plugin',
            description='Identifier plugin type (e.g. "fileidentifier", "visidentifier").',
            examples=['fileidentifier', 'visidentifier'],
        ),
    ]

    params: Annotated[
        Optional[Any],
        Field(
            alias='params',
            default=None,
            description='Plugin-specific parameters passed verbatim to the identifier plugin.',
        ),
    ]


class IAMConfig(BaseModel):
    """
    Identity and Access Manager (IAM) configuration schema.

    This schema describes the JSON configuration file for the Aos IAM,
    typically located at /etc/aos/iam.cfg .

    Several top-level fields are shared between the IAM server role (listening for connections
    from SM/CM) and the IAM client role (connecting to a main/primary IAM on a multi-node setup).
    """

    # -------------------------------------------------------------------------
    # Node identity
    # -------------------------------------------------------------------------

    node_info: Annotated[
        NodeInfoConfig,
        Field(
            alias='nodeInfo',
            description='Hardware and software description of this node, reported to the cloud.',
        ),
    ]

    # -------------------------------------------------------------------------
    # Shared TLS / provisioning fields (used by both IAM server and IAM client)
    # -------------------------------------------------------------------------

    ca_cert: Annotated[
        str,
        Field(
            alias='caCert',
            description='Path to the CA certificate file used for mutual TLS connections.',
        ),
    ]

    cert_storage: Annotated[
        str,
        Field(
            alias='certStorage',
            description='Certificate storage identifier used for IAM TLS credentials.',
            examples=['/var/aos/crypt/iam/'],
        ),
    ]

    start_provisioning_cmd_args: Annotated[
        Optional[List[str]],
        Field(
            alias='startProvisioningCmdArgs',
            default=None,
            description='Command-line (argv) of the script executed at the start of provisioning.',
            examples=[['/var/aos/start_provisioning.sh']],
        ),
    ]

    finish_provisioning_cmd_args: Annotated[
        Optional[List[str]],
        Field(
            alias='finishProvisioningCmdArgs',
            default=None,
            description='Command-line (argv) of the script executed when provisioning completes.',
            examples=[['/var/aos/finish.sh']],
        ),
    ]

    disk_encryption_cmd_args: Annotated[
        Optional[List[str]],
        Field(
            alias='diskEncryptionCmdArgs',
            default=None,
            description='Command-line (argv) of the disk encryption script run during provisioning.',
            examples=[['/bin/sh', '/var/aos/encrypt.sh']],
        ),
    ]

    deprovision_cmd_args: Annotated[
        Optional[List[str]],
        Field(
            alias='deprovisionCmdArgs',
            default=None,
            description='Command-line (argv) of the script executed during de-provisioning.',
            examples=[['/var/aos/deprovision.sh']],
        ),
    ]

    # -------------------------------------------------------------------------
    # IAM server role (SM/CM connect to this node's IAM)
    # -------------------------------------------------------------------------

    iam_public_server_url: Annotated[
        str,
        Field(
            alias='iamPublicServerURL',
            description='Listening address of the IAM public gRPC server (unauthenticated operations).',
            examples=['localhost:8090'],
        ),
    ]

    iam_protected_server_url: Annotated[
        str,
        Field(
            alias='iamProtectedServerURL',
            description='Listening address of the IAM protected gRPC server (certificate operations).',
            examples=['localhost:8089'],
        ),
    ]

    # -------------------------------------------------------------------------
    # IAM client role (multi-node: this IAM connects to a main/primary IAM)
    # -------------------------------------------------------------------------

    main_iam_public_server_url: Annotated[
        Optional[str],
        Field(
            alias='mainIAMPublicServerURL',
            default=None,
            description="""\
URL of the main (primary) IAM public gRPC server.
Required in multi-node setups where this node's IAM registers with a central IAM.""",
            examples=['main-node:8090'],
        ),
    ]

    main_iam_protected_server_url: Annotated[
        Optional[str],
        Field(
            alias='mainIAMProtectedServerURL',
            default=None,
            description="""\
URL of the main (primary) IAM protected gRPC server.
Required in multi-node setups where this node's IAM registers with a central IAM.""",
            examples=['main-node:8089'],
        ),
    ]

    node_reconnect_interval: Annotated[
        Optional[str],
        Field(
            alias='nodeReconnectInterval',
            default='10s',
            description="""\
Delay before retrying a dropped connection to the main IAM. Default: 10s.
Format: duration string (e.g. "10s", "30s", "1m").""",
            examples=['10s', '30s', '1m'],
        ),
    ]

    # -------------------------------------------------------------------------
    # Database
    # -------------------------------------------------------------------------

    working_dir: Annotated[
        str,
        Field(
            alias='workingDir',
            description='Working directory for the IAM database and runtime data.',
        ),
    ]

    migration: Annotated[
        DatabaseMigrationConfig,
        Field(
            alias='migration',
            description='Database migration paths.',
        ),
    ]

    # -------------------------------------------------------------------------
    # Certificate modules and identifier
    # -------------------------------------------------------------------------

    cert_modules: Annotated[
        Optional[List[CertModuleConfig]],
        Field(
            alias='certModules',
            default=None,
            description='List of certificate module (plugin) configurations managed by the IAM.',
        ),
    ]

    enable_permissions_handler: Annotated[
        bool,
        Field(
            alias='enablePermissionsHandler',
            description='Enable the IAM permissions handler for deployable items access-control policy enforcement.',
        ),
    ]

    identifier: Annotated[
        Optional[IdentifierConfig],
        Field(
            alias='identifier',
            default=None,
            description='Identifier plugin configuration used to resolve system/unit IDs.',
        ),
    ]
