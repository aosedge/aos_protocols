#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#

class DataSizes:
    MAX_ALERT_MESSAGE_LENGTH = 32 * 1024  # noqa: WPS432
    MAX_COMPONENT_ID_LENGTH = 100

    PHONE_LENGTH = 15
    CRC32_LENGTH = 15
    FIRST_NAME_LENGTH = 30
    LAST_NAME_LENGTH = 150
    STATUS_LENGTH = 30
    TYPES_LENGTH = 30
    MIDDLE_CHAR_FIELD_LENGTH = 100
    LONG_CHAR_FIELD_LENGTH = 200
    DESCRIPTION_LENGTH = 300
    LONG_DESCRIPTION_LENGTH = 1000
    DATA_LENGTH_32 = 32        # noqa: WPS114
    DATA_LENGTH_64 = 64        # noqa: WPS114
    DATA_LENGTH_128 = 128      # noqa: WPS114
    DATA_LENGTH_256 = 256      # noqa: WPS114
    DATA_LENGTH_512 = 512      # noqa: WPS114
    DATA_LENGTH_1000 = 1000    # noqa: WPS114
    DATA_LENGTH_10240 = 10240  # noqa: WPS114
