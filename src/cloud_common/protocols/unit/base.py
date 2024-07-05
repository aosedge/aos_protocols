#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from typing import Annotated, Union

from pydantic import BaseModel, Discriminator, Field

from cloud_common.protocols.unit.alert import AosAlerts
from cloud_common.protocols.unit.certificates import (
    AosInstallUnitCertificatesConfirmation,
    AosIssuedUnitCertificates,
    AosIssueUnitCertificates,
    AosRenewCertsNotification,
)
from cloud_common.protocols.unit.desired_status import AosDesiredStatus
from cloud_common.protocols.unit.envars import (
    AosOverrideEnvVarsRequest,
    AosOverrideEnvVarsStatuses,
)
from cloud_common.protocols.unit.header import AosUnitHeader
from cloud_common.protocols.unit.log import AosPushLog, AosRequestLog
from cloud_common.protocols.unit.monitoring import AosMonitoring
from cloud_common.protocols.unit.state import (
    AosNewState,
    AosStateAcceptance,
    AosStateRequest,
    AosUpdateState,
)
from cloud_common.protocols.unit.unit_status import AosUnitStatus


class AosUnitMessage(BaseModel):
    """Unit message model."""

    header: Annotated[
        AosUnitHeader,
        Field(
            description='Aos Unit-Cloud message header',
        ),
    ]
    data: Annotated[  # noqa: WPS110
        Union[
            AosAlerts,
            AosMonitoring,
            AosUnitStatus,
            AosDesiredStatus,
            AosNewState,
            AosStateRequest,
            AosStateAcceptance,
            AosUpdateState,
            AosRequestLog,
            AosPushLog,
            AosOverrideEnvVarsRequest,
            AosOverrideEnvVarsStatuses,
            AosRenewCertsNotification,
            AosRenewCertsNotification,
            AosIssuedUnitCertificates,
            AosIssueUnitCertificates,
            AosInstallUnitCertificatesConfirmation,
        ],
        Field(
            description='message payload',
        ),
        Discriminator('message_type'),
    ]
