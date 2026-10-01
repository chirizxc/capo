"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

"""<p>The day of the week on which a weekly sync runs. Valid values are the standard English day names, for example, MONDAY or TUESDAY.</p>"""
DayOfWeek: TypeAlias = Literal[
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DayOfWeek) -> str:
    return value


def deserialize_json(data: str) -> DayOfWeek:
    return cast(DayOfWeek, data)
