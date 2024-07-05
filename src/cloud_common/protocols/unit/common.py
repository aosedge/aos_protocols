#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from typing import Annotated

from pydantic import BaseModel, Field


class AosErrorInfo(BaseModel):
    """
    AosUnit error info structure.

    Encapsulates a structure for AosUnit error info.
    All fields are optional. In this case treated as no error.
    """

    aos_code: Annotated[
        int,
        Field(
            default=None,
            alias='aosCode',
            title='Aos error code',
            description='AosCore error code.',
        ),
    ]

    exit_code: Annotated[
        int,
        Field(
            default=None,
            alias='exitCode',
            title='Exit code',
            description='Module error code.',
        ),
    ]

    message: Annotated[
        str,
        Field(
            default=None,
            title='Error message',
            description='Text of the error description.',
        ),
    ]


class AosHostRecord(BaseModel):

    ip: Annotated[
        str,
        Field(
            alias='ip',
            title='IP address',
            description='IP address.',
        ),
    ]

    hostname: Annotated[
        str,
        Field(
            alias='hostname',
            title='Hostname',
            description='The hostname for the IP address.',
        ),
    ]


class AosDeviceInfo(BaseModel):

    name: Annotated[
        str,
        Field(
            alias='name',
            description='Name of the device.',
        ),
    ]

    host_devices: Annotated[
        list[str],
        Field(
            alias='hostDevices',
            description='List of host devices.',
        ),
    ]

    shared_count: Annotated[
        int,
        Field(
            alias='sharedCount',
            default=0,
            ge=0,
            description='The count of shared devices that can be used in one time. 0 means no restrictions.',
        ),
    ]

    groups: Annotated[
        list[str],
        Field(
            default=None,
            description='List of associated groups.',
        ),
    ]


class AosFileSystemMount(BaseModel):

    destination: Annotated[
        str,
        Field(
            alias='destination',
            description="The mount's destination.",
        ),
    ]

    source: Annotated[
        str,
        Field(
            default=None,
            alias='source',
            description="The mount's source.",
        ),
    ]

    mount_type: Annotated[
        str,
        Field(
            default=None,
            alias='type',
            description="The mount's type.",
        ),
    ]

    options: Annotated[
        list[str],
        Field(
            default=None,
            alias='options',
            description="The mount's options.",
        ),
    ]


class AosAlertConfig(BaseModel):

    min_time: Annotated[
        int,
        Field(
            alias='minTime',
            description='Minimum time (window) in seconds.',
        ),
    ]

    min_threshold: Annotated[
        int,
        Field(
            alias='minThreshold',
            description='Minimum threshold to stop alerting.',
        ),
    ]

    max_threshold: Annotated[
        int,
        Field(
            alias='maxThreshold',
            description='Threshold to trigger the alert.',
        ),
    ]


TypeAosErrorInfoOptional = Annotated[
    AosErrorInfo,
    Field(
        default=None,
        alias='errorInfo',
        description='Error information. Absense means no error.',
    ),
]
