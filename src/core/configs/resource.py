#
#  Copyright (c) 2026 EPAM Systems Inc.
#
from typing import Annotated, List, Optional

from pydantic import BaseModel, Field, RootModel


class Mount(BaseModel):
    """Filesystem mount entry."""

    destination: Annotated[
        str,
        Field(
            alias='destination',
            description='Mount destination path.',
            examples=['/dev/bus/usb'],
        ),
    ]

    type: Annotated[
        str,
        Field(
            alias='type',
            description='Filesystem type (e.g. "bind", "tmpfs").',
            examples=['bind', 'tmpfs'],
        ),
    ]

    source: Annotated[
        str,
        Field(
            alias='source',
            description='Source path.',
            examples=['/dev/bus/usb'],
        ),
    ]

    options: Annotated[
        Optional[List[str]],
        Field(
            alias='options',
            default=None,
            description='Mount options.',
            examples=[['ro', 'bind'], ['rbind', 'rprivate']],
        ),
    ]


class Host(BaseModel):
    """Extra host-to-IP mapping."""

    hostname: Annotated[
        str,
        Field(
            alias='hostname',
            description='Hostname to resolve.',
            examples=['Kuksa'],
        ),
    ]

    ip: Annotated[
        str,
        Field(
            alias='ip',
            title='IP',
            description='IP address the hostname resolves to.',
            examples=['10.0.0.100'],
        ),
    ]


class ResourceInfo(BaseModel):
    """Description of a single named resource available for allocation."""

    name: Annotated[
        str,
        Field(
            alias='name',
            description='Unique resource identifier.',
            examples=['bluetooth', 'video'],
        ),
    ]

    shared_count: Annotated[
        Optional[int],
        Field(
            alias='sharedCount',
            default=0,
            ge=0,
            description='Maximum number of allocations for this resource. 0 means unlimited.',
        ),
    ]

    groups: Annotated[
        Optional[List[str]],
        Field(
            alias='groups',
            default=None,
            description='Group names attached to this resource.',
            examples=[['video', 'audio']],
        ),
    ]

    mounts: Annotated[
        Optional[List[Mount]],
        Field(
            alias='mounts',
            default=None,
            description='Filesystem mounts attached to this resource.',
        ),
    ]

    envs: Annotated[
        Optional[List[str]],
        Field(
            alias='envs',
            default=None,
            description='Environment variables attached to this resource in KEY=VALUE form.',
            examples=[['MY_VAR=1', 'OTHER=abc']],
        ),
    ]

    hosts: Annotated[
        Optional[List[Host]],
        Field(
            alias='hosts',
            default=None,
            description='Extra host-to-IP mappings attached to this resource.',
        ),
    ]

    devices: Annotated[
        Optional[List[str]],
        Field(
            alias='devices',
            default=None,
            description="""\
List of devices attached to this resource.
Format: <src-path>:<dst-path> (e.g. "/dev/video0:/dev/video").
src-path is the path on the host, dst-path is the path inside the container. If dst-path is omitted, it defaults to src-path.""",
            examples=[['/dev/video0:/dev/video', '/dev/snd']],
        ),
    ]


class ResourcesConfig(RootModel[List[ResourceInfo]]):
    """
    Resources configuration schema.

    This schema describes the JSON resources configuration file for the Aos Service Manager,
    typically located at /etc/aos/resources.cfg .

    The file contains a JSON array of resource descriptors. Each entry declares a named
    resource along with the OS groups, mounts, environment variables, hosts, and device
    nodes that are injected into a service container when the resource is allocated.
    """
