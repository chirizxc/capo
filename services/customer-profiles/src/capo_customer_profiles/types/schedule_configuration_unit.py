"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ScheduleConfigurationUnit``."""

from typing import Literal, TypeAlias, cast

ScheduleConfigurationUnit: TypeAlias = Literal["HOURLY",]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleConfigurationUnit) -> str:
    return value


def deserialize_json(data: str) -> ScheduleConfigurationUnit:
    return cast(ScheduleConfigurationUnit, data)
